
def csv_to_tsv(input_file, output_file):
    with open("ds.csv", mode='r', newline='', encoding='utf-8') as in_f , \
        open("ds.tsv", mode='w', newline='', encoding='utf-8') as out_f:

        for line in in_f:
            new_line = line.replace(',', '\t')
            out_f.write(new_line)

if __name__ == "__main__":
    csv_to_tsv('ds.csv', 'ds.tsv')