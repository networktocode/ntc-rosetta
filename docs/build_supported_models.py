from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Type, Union


from ntc_rosetta import get_driver
from ntc_rosetta.yang import get_data_model

from yangify.linter import ContainerLinterResult, RootLinter, RootLinterResult
from yangify.parser import Parser, RootParser
from yangify.translator import RootTranslator, Translator

from yangson.schemanode import (
    GroupNode,
    LeafListNode,
    LeafNode,
    SchemaNode,
    SchemaTreeNode,
)

models = ("openconfig",)
drivers = ("ios", "junos")

LintClass = Union[
    Type[Parser], Type[RootParser], Type[Translator], Type[RootTranslator]
]


@dataclass
class LinterResult:
    metadata: Dict[str, Any]
    implements: List[str]


class LinterPathResult(Dict[str, LinterResult]):
    pass


class LinterPlatformResult(Dict[str, LinterPathResult]):
    pass


def _process_linter_child(linted: ContainerLinterResult) -> LinterPathResult:
    result: LinterPathResult = LinterPathResult()
    result[linted.path] = LinterResult(
        metadata=linted.metadata, implements=linted.implements
    )
    for child in linted.children.values():
        result.update(_process_linter_child(child))
    return result


def _process_linter(linted: RootLinterResult) -> LinterPathResult:
    result: LinterPathResult = LinterPathResult()
    for child in linted.children.values():
        result.update(_process_linter_child(child))
    return result


@dataclass
class SchemaResult:
    metadata: Dict[str, Any]
    implemented: bool


class PlatformResultsSchema(Dict[str, SchemaResult]):
    pass


code_style = (
    "style=\"font-family:'Lucida Console', monospace; font-size: 12px; line-height: 1\""
)


class ResultsSchema(Dict[str, PlatformResultsSchema]):
    def to_html_table(self, title: str) -> str:
        text = f"{title}\n{'=' * len(title)}\n\n"
        text += ".. raw:: html\n\n"
        text += "    <table border=1>\n"
        text += '      <col width="60%"><col width="20%"><col width="20%">'
        text += "      <tr>\n"
        text += "        <th>path</th>\n"
        for platform in drivers:
            text += f"        <th>{platform}</th>\n"
        text += "      </tr>\n"
        for k, v in self.items():
            text += "      <tr>\n"
            text += f"        <td>{k}</td>\n"

            for platform in drivers:
                text += "        <td>"
                text += "&#x2705" if v[platform].implemented else "\u274c"
                if v[platform].metadata:
                    text += f" <div {code_style}>{v[platform].metadata}</div>"
                text += "    </td>\n"
            text += "      </tr>\n"
        text += "    </table>\n"
        return text


def _process_schema_child(
    schema: SchemaNode, linted: Dict[str, LinterPathResult]
) -> ResultsSchema:
    results = ResultsSchema()
    results[schema.data_path()] = PlatformResultsSchema()
    for platform, linted_platform in linted.items():
        if schema.data_path() in linted_platform:
            r = SchemaResult(
                implemented=True, metadata=linted_platform[schema.data_path()].metadata
            )
        else:
            r = SchemaResult(implemented=False, metadata={})
        results[schema.data_path()][platform] = r

    for child in schema.children:
        if isinstance(child, LeafNode):
            results[child.data_path()] = PlatformResultsSchema()
            parent = child.data_parent().data_path()
            for platform, linted_platform in linted.items():
                r = SchemaResult(implemented=False, metadata={})
                if parent in linted_platform:
                    if child.name in linted_platform[parent].implements:
                        r = SchemaResult(implemented=True, metadata={})
                results[child.data_path()][platform] = r
        elif isinstance(child, (GroupNode, LeafListNode)):
            pass
        else:
            results.update(_process_schema_child(child, linted))

    return results


def _process_schema(
    schema: SchemaTreeNode, linted: LinterPlatformResult
) -> ResultsSchema:
    results = ResultsSchema()
    for child in schema.children:
        results.update(_process_schema_child(child, linted))
    return results


def main() -> None:
    for processor_type in ["parser", "translator"]:
        linter_result = LinterPlatformResult()
        for model in models:
            dm = get_data_model(model)
            for driver in drivers:
                d = get_driver(driver, model)
                r = RootLinter.lint(getattr(d, processor_type), dm, True, set())
                linter_result[driver] = _process_linter(r)

            schema_result = _process_schema(dm.schema, linter_result)

            filepath = Path(__file__).parent.joinpath(
                "models", "matrix", f"{model}_{processor_type}.rst"
            )
            with open(filepath, "w+") as f:
                f.write(schema_result.to_html_table(f"{model} {processor_type}"))


if __name__ == "__main__":
    main()
