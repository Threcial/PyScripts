import os

# path
filepath = os.path.abspath(__file__)
filepath = filepath.replace("UpdateListmd.py", "article\\list.md")
articlepath = filepath.replace("\\list.md", "")
flag = 0

# all files in article and remove needless
Files = os.listdir(articlepath)
remove_list = ["imgs", "list.md"]
for i in remove_list:
    Files.remove(i)
Files_length = len(Files)
print(f"现有文章 {Files_length} 个\n")

# contrast
with open(filepath, "r", encoding= "utf-8") as Listmd :
    title = [i.strip() for i in Listmd]
    title_length = len(title)
    print(f"原有记录 {title_length} 个")
    
    set1 = set(Files)
    set2 = set(title)
    new_files = set1 - set2
    del_files = set2 - set1
    same_files = set1 & set2
    set3 = same_files | new_files
    fin_list = list(set3)

    # add files
    if new_files:
        flag = 1
        new_files_length = len(new_files)
        print(f"新增记录 {new_files_length} 个 : ", end="")
        for i in new_files:
            print(i, end=" ; ")
        print("\n")

    # del files
    if del_files:
        flag = 1
        del_files_length = len(del_files)
        print(f"删除记录 {del_files_length} 个 : ", end="")
        for i in del_files:
            print(i, end=" ; ")
        print("\n")

if flag == 0:
    print("完全一致，无需同步")
    input("\n\nPress any key to continue")
else:
    # synchronization new files
    with open(filepath, "w", encoding= "utf-8") as n :
        for i in range(len(fin_list)):
            fin_list[i] += "\n"
        n.writelines(fin_list)
    print(f"同步后有记录 {len(fin_list)} 个")
    input("\n\nPress any key to continue...")