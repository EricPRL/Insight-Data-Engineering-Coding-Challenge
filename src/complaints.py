import sys
import csv
from collections import Counter


class solution:
    
    def __init__(self):
        
        self.record_dict= {}
        
        # key (product,year)
        self.key = []
        
    def add_company(self, product, year, company):
        if (product,year) in self.record_dict.keys():
            self.record_dict[(product,year)].append(company)
        else:
            self.record_dict[(product,year)]= [company]
    

    def calculation(self):
        
        # Sort the key (product,year)
        new_keys = sorted(self.record_dict.keys())
        
        output = []
        
        for key in new_keys:
            
            company_records = self.record_dict[key]
            
            # Use all the lower case for the company names.
            company_records = map(str.lower, company_records)
    
            number_records = Counter(company_records)
            
            company_list = number_records.keys()
            
            # Number of unqiue companies for each year and product
            companies = len(set(company_list))
            
            company_numbers = number_records.values()
            
            # Number of total complaints
            total_number = sum(company_numbers)
            
            # Get the max number of the company
            max_num = max(company_numbers)
            
            highest = max_num/total_number
            
            # Get the highest percentage 
            result = round(highest*100,0)
            
            result = int(result)
            
            product = key[0]
            
            year = key[1]
            
            # Put the list together
            output.append([product,year,str(total_number),str(companies),str(result)])
        
        return output
    

        
        
def get_record(filename):

    # Generate record_dict = {}
    record_dict = solution()

    with open(filename) as input_file:
        data = csv.reader(input_file, delimiter=',')

        count = 0
        for row in data:
            if count>0:
                product = row[1].lower()
                
                # check for ","
                if "," in product:
                    product = '"'+product+'"'
                
                time = row[0]

                year = time[0:4]

                company = row[7].lower()

                # Genarate key and add the company, key =(product,year)

                record_dict.add_company(product, year, company)
        
            count += 1 
            
        return record_dict   
    
    
def get_report(output,filename):
    with open(filename,'w',newline='') as output_csv:
        csv_writer=csv.writer(output_csv,delimiter=',')
        csv_writer.writerows(output)
    

# Main     
    
if __name__ == "__main__":
    input_filename=sys.argv[1]
    output_filename=sys.argv[2]
    
    complaint_records = get_record(input_filename)
    
    results = complaint_records.calculation() 
    
    get_report(results,output_filename)
            
