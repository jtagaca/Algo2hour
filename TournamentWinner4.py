#Time is O(n) Space is O(k) k is the number of elements that is dependent on how many teams there are

def tournamentWinner(competitions, results):

	
	BestTeam=""
	winnerMap={BestTeam: 0}
	for i, compete in enumerate(competitions):
		lefteam, rightteam=compete
		if results[i]==1:
			winner=lefteam
		else:
			winner=rightteam
		update(winner, winnerMap,3)
		
		if winnerMap[BestTeam]<winnerMap[winner]:
			BestTeam=winner
		
    return BestTeam
def update(winner,winnerMap,points):
	if winner not in winnerMap:
		winnerMap[winner]=0
	winnerMap[winner]+=points
	
	