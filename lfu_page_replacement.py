# Least Frequently Used Algorithm

# get the page sequence from the user and assign those pages to a list
def get_pages_from_user(no_of_pages):
    reference_sequence = []
    for i in range(0, no_of_pages):
        page_id = int(input(f"Enter Page ID {i+1}: "))
        reference_sequence.append(page_id)
    return reference_sequence

# function for implement least frequently used algorithm
def lfu_page_replacement():
    page_faults = 0 # initially number of page faults is set to 0

    no_of_frames = int(input("Enter the number of frames: "))
    no_of_pages = int(input("Enter the number of pages in the sequence: "))
    
    page_frequencies = {}
    page_replacement = []

    reference_sequence = get_pages_from_user(no_of_pages)

    # get all unique pages that present in the sequence
    unique_pages = list(set(reference_sequence)) 

    # assign the frequency of all unique pages to 0 at initial
    for i in range(0, len(unique_pages)):
        page_frequencies[unique_pages[i]] = 0

    # assign all values of page replacement list to 0 at initial
    page_replacement = [[0 for _ in range(no_of_pages)] for _ in range(no_of_frames)]

    # get current page frame block
    temp_frame_block = [frame_block[0] for frame_block in page_replacement]

    in_out_seq = []

    for i in range (0, no_of_pages):
        if reference_sequence[i] in temp_frame_block:
            pass
        else:
            page_faults += 1
            temp_frequencies = []
            for j in range(0, len(temp_frame_block)):
                if temp_frame_block[j] != 0:
                    temp_frequencies.append(page_frequencies[temp_frame_block[j]])
                else:
                    # if the frame block have unassigned frames, freqeuency of that set to max number
                    temp_frequencies.append(no_of_pages) 

            temp_min_freq = min(temp_frequencies)
            flag = 1
            for item in temp_frame_block:
                if item not in in_out_seq:
                    in_out_seq.append(item)

            min_freq_pages = []
            # check if there other min frequecies in the that frame block
            for element in temp_frame_block:
                if element != 0:
                    if page_frequencies[element] == temp_min_freq:
                        min_freq_pages.append(element)
                else:
                    flag = 0
                    temp_frame_block[temp_frame_block.index(element)] = reference_sequence[i]
                    break

            # if there are more than one page with same min frequency then go to FIFO
            if len(min_freq_pages) > 1 and flag:
                for page in in_out_seq:
                    if page in min_freq_pages:
                        in_out_seq.remove(page)
                        if reference_sequence[i] not in in_out_seq:
                            in_out_seq.append(reference_sequence[i])
                        else:
                            in_out_seq.remove(reference_sequence[i])
                            in_out_seq.append(reference_sequence[i])
                        temp_frame_block[temp_frame_block.index(page)] = reference_sequence[i]
                        break

            elif len(min_freq_pages) == 1 and flag:
                temp_frame_block[temp_frame_block.index(min_freq_pages[0])] = reference_sequence[i]

        # increase the freqeuncy of the particular page
        page_frequencies[reference_sequence[i]] += 1

        for k in range(0, no_of_frames):
                page_replacement[k][i] = temp_frame_block[k]

    print(f"Reference Sequence: {reference_sequence}")
    print(f"Page Frequencies: {page_frequencies}")
    print(f"Min Freq Pages: {min_freq_pages}")
    print(f"Page Faults: {page_faults}")
    print(f"Page Replacement: \n")
    print("Ref_Seq: ", end="")
    for item in reference_sequence:
        print(item, end="")
        print("\t", end="")
    print("")
    print("-------------------------------------------------------------------------------------------------------------")
    for i, row in enumerate(page_replacement):
        print(f"Frame {i+1}: ", end="")
        for item in row:
            print(f"{item}\t", end="")
        print("")

lfu_page_replacement()
