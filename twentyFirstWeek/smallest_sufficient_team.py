class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        dp = {0: []}
        skill_dict = {v: i for i, v in enumerate(req_skills)}
        for i, person in enumerate(people):
            his_skill = 0
            for skill in person:
                if skill in skill_dict:
                    his_skill |= 1 << skill_dict[skill]
            for skills, need in list(dp.items()):
                with_him = his_skill | skills
                if with_him not in dp or len(dp[with_him]) > len(need) + 1:
                    dp[with_him] = need + [i]
        return dp[(1<<len(req_skills))-1]