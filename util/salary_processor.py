# use regex to extract the salary information from the job description
import re

#if yr, year, annually, per annum, per year, in text, extract the number as annual salary
#if hr, hourly, per hour, in text, extract the number as hourly salary then multiply by 40 hours per week and 52 weeks per year
#if k, in text, extract the number and multiply by 1000
#ignore cad, $, +, /
#if - in text, extract the two numbers and take the average
#if to in text, extract the two numbers and take the average
#if ~ in text, extract the two numbers and take the average
#any non-alpha numeric character, replace with space
#if only text, set to nan

def extract_salary(text):
    print(f"{text=}")
    #replace , with nothing
    text = re.sub(r",", "", text)
    
    #any non-alpha numeric character, replace with space, but dont replace -, ~
    text = re.sub(r"[^a-zA-Z0-9\s\-~.]", " ", text)
    
    #if only text or spaces, set to nan
    if re.match(r"^[^\d]+$", text):
        return 0
    
    #if yr, year, annually, per annum, per year, in text, extract the number as annual salary
    if re.search(r"(yr|year|annually|per annum|per year)", text, re.IGNORECASE):
        #if k in text, extract the number and multiply by 1000
        if re.search(r"k", text, re.IGNORECASE):
            salary = re.search(r"\d+", text).group()
            return int(salary) * 1000
        salary = re.search(r"\d+", text).group()
        return int(salary)

    #if hr, hourly, per hour, in text, extract the number as hourly salary then multiply by 40 hours per week and 52 weeks per year
    if re.search(r"(hr|hourly|per hour)", text, re.IGNORECASE):
        #if k in text, extract the number and multiply by 1000
        if re.search(r"k", text, re.IGNORECASE):
            salary = re.search(r"\d+", text).group()
            return int(salary) * 1000
        salary = re.search(r"\d+", text).group()
        return int(salary) * 40 * 52
    
    #check how many numbers are in the text
    numbers = re.findall(r"\d+", text)
    if len(numbers) == 2:
        #what if the salary is in the form of a range
        if "-" in text:
            salary1, salary2 = re.findall(r"\d+", text)
            return (int(salary1) + int(salary2)) // 2    
        if "to" in text: 
            salary1, salary2 = re.findall(r"\d+", text)
            return (int(salary1) + int(salary2)) // 2
        
        if "~" in text:
            salary1, salary2 = re.findall(r"\d+", text)
            return (int(salary1) + int(salary2)) // 2
    
    if re.search(r"k", text, re.IGNORECASE):
        salary = re.search(r"\d+", text).group()
        return int(salary) * 1000
    
    #if number in text, extract the number
    if re.search(r"\d+", text):
        salary = re.search(r"\d+", text).group()
        #if number is less than 50, assume it is hourly
        if int(salary) < 50:
            return int(salary) * 40 * 52
        #if number is less than 200, assume its annual
        if int(salary) < 200:
            return int(salary) * 1000
        return int(salary)
    
    return 0