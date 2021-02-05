class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split("/")
        canonical = []

        for char in files:
            to_append = char != "" and char != "." and char != ".."
            if char.isalpha() or to_append:
                canonical.append(char)
            elif char == "..":
                if canonical:
                    canonical.pop()

        return "/" + "/".join(canonical)