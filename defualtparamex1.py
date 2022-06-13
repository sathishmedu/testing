def dispstuddet(sno,sname,marks,crs="PYTHON",cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}".format(sno,sname,marks,crs,cnt))
#main prog
print("-"*40)
print("Student information")
print("-"*40)
print("\tsno\tsname\tmarks\tcrs\tcnt")
dispstuddet(10,"Sunny",87.56)
dispstuddet(20,"Nandu",93.45)
dispstuddet(30,"Bunny",58.49,"JAVA")
dispstuddet(40,"Nani","DS","US")