sub1 = ("Maths" , "Physics" , "Chemistry")

sub2= ("Telugu" , "Sanskrit" , "English")



print("Recipei 1" ,sub1 )

print("Nmae:" , sub1[0])

print("Cusine:" , sub1[1])

print("Difficylty:" , sub1[-1])



all_recipes = (sub1 ,sub2)

print("First subject name:" , all_recipes[0][0])

print("Second subject name" , all_recipes[1][2] , "mins")

print("SUBLECT details (sliced):" , sub1[1:3])




print("Subject  Details")

for details in sub1:
    print("" , details)



Monday = {"Maths" , "Physics" , "Chemistry" , "Social"}

Tuesday = {"Telugu" , "Sanskrit" , "English" , "Hindi"}


print("Subjects to be read on monday:" , Monday)

print("Subjects to be read on tuesday:" ,Tuesday)





all_subjects = Monday.union(Tuesday)

common_subjects = Monday.intersection(Tuesday)

difference_of_subjects =Monday.difference(Tuesday)

unique_to_each = Monday.symmetric_difference(Tuesday)





print("All subjects union" ,all_subjects)

print("Common subjects (intersectipn)" ,common_subjects)

print("only in subjects(difference):" , difference_of_subjects)

print("NOT shared subjects(sym.diifference):" , unique_to_each)


























