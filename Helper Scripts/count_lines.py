num_lines=0
with open("cleaned_train_en_withoutEmptyLines","r",encoding='utf-8') as f:
    for line in f: 
        num_lines=num_lines+1
		
print(num_lines)