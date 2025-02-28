def max_bouquet_cost(budgets):
    flower_costs = [2**i for i in range(101)]
    results = []

    for budget in budgets:
        max_spent = -1
        found = False

        for i in range(len(flower_costs)):
            if flower_costs[i] > budget:
                break
            for j in range(i+1, len(flower_costs)):
                if flower_costs[i] + flower_costs[j] > budget:
                    break
                for k in range(j+1, len(flower_costs)):
                    total_cost = flower_costs[i] + flower_costs[j] + flower_costs[k]
                    if total_cost > budget:
                        break
                    max_spent = max(max_spent, total_cost)
                    found = True
        results.append(max_spent if found else -1)

    return results


n = int(input())
budgets = [int(input()) for i in range(n)]

output = max_bouquet_cost(budgets)

for res in output:
    print(res)