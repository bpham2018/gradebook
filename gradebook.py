def individual_averages( grades ):
	
	averagesList = []
	
	for row in grades:
	
		average = 0
		
		for items in row:
		
			average += items
			
		average = average/len( row )
		
		averagesList.append( average )
		
	return averagesList

def class_Average( grades ):

	numberOfScores = 0
	
	for row in grades:
	
		for items in row:
		
			numberOfScores += 1

	classAverage = 0

	for row in grades:
	
		for items in row:

			classAverage += items
			
	classAverage = classAverage/numberOfScores	
			
	return classAverage

grades = [ [ 100, 99, 98, 99, 100 ],
		   [ 95, 0, 85, 70 ],
		   [ 90, 91, 95, 97, 99 ] ]
		   
averagesList = individual_averages( grades )

classAverage = class_Average( grades )


print( "Student 1's average is " + str( averagesList[ 0 ] ) )
print( "Student 2's average is " + str( averagesList[ 1 ] ) )
print( "Student 3's average is " + str( averagesList[ 2 ] ) )

print( "The class average is " + str( classAverage ) )

