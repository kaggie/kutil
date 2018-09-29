def compare_path_files(path1 = './', path2='git/'):
    import glob
    import filecmp
    files1 = glob.glob(path1+'*')
    files2 = glob.glob(path2+'*')
    files2new = []
    for filename in files2:
        files2new.append(filename.split('/')[-1])
    files2 = files2new
    samelist = []
    difflist = []
    for filename in files1:
        #print(filename.split('/')[-1])
        filesplit = filename.split('/')[-1]
        if filesplit in files2:
            print(filesplit)
            answer = filecmp.cmp(path1+filesplit, path2+filesplit )
            print(answer)
            if answer:
                samelist.append(filesplit)
        else:
            difflist.append(filesplit)
    return samelist, difflist
    
    
## compare two text files.  returns line by line analysi
def compare_file_text(file1 = '1.txt', file2= '2.txt'):
    import numpy as np  ##oh, my eyes!  real developers import within functions, unintentionally breaking tools for some
    with open(file1,'r') as f1:
        lines1 = f1.readlines()

    with open(file2,'r') as f2:
        lines2 = f2.readlines()    

    oldline1 = ''
    oldline2 = ''
    newline = ''

    xi = -1
    yi = -1

    equal_lines = {}
    new_lines1 = ''
    new_lines2 = ''
    new_lines_all1 = {}
    new_lines_all2 = []
    new_lines_all2 = {}
    if len(lines1) != len(lines2):
        print('Watch out for extra lines not being returned')
    for count in range(min(len(lines1), len(lines2))):
        xi = xi+1
        yi = yi+1    
        line1 = lines1[xi]
        line2 = lines2[yi]
        if xi > 0:
            oldline1 = lines1[xi-1]
        if yi > 0:
            oldline2 = lines2[yi-1]                
        if line1 == line2:
            #print('a',line1.strip(), line2.strip(), xi, yi)
            equal_lines[xi] = line1
        elif line1 == oldline2:
            #print('b', line1.strip(), oldline2.strip(), xi, yi)
            yi = yi-1
            new_lines2 = new_lines2+oldline2
        elif line2 == oldline1:
            #print('c', line2.strip(), oldline1.strip(), xi, yi)
            xi = xi-1
            new_lines1 = new_lines1+oldline1
        else:        
            if line1 in lines2:
                eqat = np.argwhere(line1==np.array(lines2))[0][0]
                new_lines_all1[xi] = lines2[yi:eqat]
                #print('equal at ', str(xi), str(eqat))
                yi = eqat-1
                xi = xi-1
            elif line2 in lines1:
                eqat = np.argwhere(line2==np.array(lines1))[0][0]
                new_lines_all2[xi] = lines1[xi:eqat]
                xi = eqat-1
                yi = yi-1
                #print('equal at ', str(yi), str(eqat))
            else:
                pass
                #print('line is not equal ', line1.strip(), line2.strip())
            oldline1 = line1
            oldline2 = line2
            print('skip')
        if yi > len(lines2):
            break
        if xi > len(lines1):
            break        
    return equal_lines, new_lines_all1, new_lines_all2
    #print(xi, yi)    
        
