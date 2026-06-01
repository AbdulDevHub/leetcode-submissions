class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for index, email in enumerate(emails):
            local, domain = email.split("@")
            emails[index] = local.split("+")[0].replace(".", "") + "@" + domain
        return len(set(emails))