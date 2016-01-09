from os import listdir
import os.path

alladf = listdir(".")

for adf in alladf:
	if adf.find(".adf") != -1:
		if adf.find("(Disk") == -1:
			#print(adf, "is a single-disk game")
			fname = adf.replace(".adf",".uae")
			
			if os.path.isfile(fname):
				output = open(fname, "w")
			else:
				output = open(fname, "a")
			
			fileObj = open("template.uae","r")
			
			print("writing config file ", fname)
			
			for line in fileObj:
				if line.find("DISK1") != -1:
					newline = line.replace("DISK1", adf)
					#print(newline)
					output.write(newline)
				elif line.find("NDISKS") != -1:
					newline = line.replace("NDISKS","2")
					output.write(newline)
				else:
					output.write(line)
									
			output.close()	
			fileObj.close()
		else: 
			if adf.find("(Disk 1") != -1:
				#print(adf, " is part of a multi-disk game")
				#print (adf, " is the first of a multi-disk game")
			
				ndisk = adf[adf.rfind("(Disk 1 of")+11]
				fname = adf.replace("(Disk 1 of "+ndisk+")","")
				fname = fname.replace(".adf",".uae")
				print("writing config file ",fname)
				if os.path.isfile(fname):
					output = open(fname, "w")
				else:
					output = open(fname, "a")
				
				fileObj = open("template.uae","r")
		
				for line in fileObj:
					if line.find("DISK1") != -1:
						newline = line.replace("DISK1", adf)
						#print(newline)
						output.write(newline)
					elif line.find("DISK2") != -1:
						newadf = adf.replace("Disk 1","Disk 2")
						newline = line.replace("DISK2", newadf)
						#print(newline)
						output.write(newline)
					elif line.find("DISK3") != -1 and int(ndisk) > 2:	
						newadf = adf.replace("Disk 1","Disk 3")
						newline = line.replace("DISK3", newadf)
						#print(newline)
						output.write(newline)
					elif line.find("DISK4") != -1 and int(ndisk) > 3:
						newadf = adf.replace("Disk 1","Disk 4")
						newline = line.replace("DISK4", newadf)
						#print(newline)
						output.write(newline)
					elif line.find("NDISKS") != -1:
						newline = line.replace("NDISKS",ndisk)
						output.write(newline)
					else:
						output.write(line)
				
				output.close()	
				fileObj.close()
