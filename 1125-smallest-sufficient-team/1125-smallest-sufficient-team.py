class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skills = {skill:[] for skill in req_skills}
        power = {req_skills[i]: i for i in range(len(req_skills))}
        code = {i:0 for i in range(len(people))}
        for i in range(len(people)):
            p = people[i]
            mask = 0
            for skill in p:
                skills[skill].append(i)
                mask += 2**(power[skill])
            code[i] = mask
        states = deque([(0, [])])
        goal = 2**(len(req_skills))-1
        ans = None
        while ans is None:
            state, t = states.popleft()
            j = 0
            while (state>>j)&1 == 1:
                j += 1
            addSkill = req_skills[j]
            for i in skills[addSkill]:
                ncode = state|code[i]
                nt = t + [i]
                if ncode == goal:
                    ans = nt
                states.append((ncode, nt))
        return ans