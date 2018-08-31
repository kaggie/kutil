def pathcompare(path1 = './', path2='git/'):
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
    
        
