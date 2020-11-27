def extract_log_info(log_file = "log.txt"):
    with open(log_file, 'r') as log_info:
        new_name, new_score = [i.strip('\n') for i in log_info.readlines()[:2]]

    new_score = int(new_score)
    return new_name, new_score

def update_leaderboards(new_name, new_score, lb_file = "Leaderboards.txt"):
    cur_index = None
    with open(lb_file, 'r') as lb_info:
        
        lb_lines = lb_info.readlines()
        lb_lines_cp = list(lb_lines) # Make a copy for iterating over
        for line in lb_lines_cp:
                        
            
            
            if 'Leaderboard' in line or line == '\n':
                continue

            # Now we're at the numbers
            position, name, score = [ i for i in line.split() ]
            

            if new_score > int(score):
                cur_index = lb_lines.index(line)
                cur_place = int(position.strip(')'))
                break

        # If you have reached the bottom of the leaderboard, and there
        # are no scores lower than yours
        if cur_index is None:
            
            # last_place essentially gets the number of entries thus far
            last_place = int(lb_lines[-1].split()[0].strip(')'))
            entry = "{}) {}\t{}\n".format((last_place+1), new_name, new_score)
            lb_lines.append(entry)
        else: # You've found a score you've beaten
            entry = "{}) {}\t{}\n".format(cur_place, new_name, new_score)
            lb_lines.insert(cur_index, entry)

            lb_lines_cp = list(lb_lines) # Make a copy for iterating over
            for line in lb_lines_cp[cur_index+1:]:
                if len(line.split()) < 2: continue
                position, entry_info = line.split(')', 1)
                new_entry_info = str(int(position)+1) + ')' + entry_info
                lb_lines[lb_lines.index(line)] = new_entry_info

    with open(lb_file, 'w') as lb_file_o:
        lb_file_o.writelines(lb_lines)


if __name__ == '__main__':
    name, score = extract_log_info()
    update_leaderboards(name, score)