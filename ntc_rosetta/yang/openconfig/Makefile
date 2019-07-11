.PHONY: clean-regexes
clean-regexes:
	find release -type f -exec sed -i "s/'\^/'/g" {} \;
	find release -type f -exec sed -i "s/\$$'/'/g" {} \;

.PHONY: check-anchors
check-anchors:
	find release -name "*.yang" -exec grep -nH \\^ {} \;
	find release -name "*.yang" -exec grep -nH \\$$ {} \;
