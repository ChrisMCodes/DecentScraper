#
# @author: ChrisMCodes
#
# purpose: mostly just a general webscraper
# (with a few fun features after the scrape)
# Users can export scraped data to txt
# or CSV after scraping.
#


# fun fact: my IDE doesn't seem to recognize the shebang *facepalm*
#!/usr/bin/env python3
# change python3 to python in the shebang above for Windows environments
#

# imports
import os
import sys
import time
from bs4 import BeautifulSoup
import requests


#
# This is the scraper class
#
# It prompts for a site and class to scrape
# (future iterations of this may have more than just class scraping)
# then returns the data, as well as the number of results.
#
# Results can be outputted to a CSV or TXT
#
class Pagedata:
    page = ""        # stores the URL of the page being scraped
    cls = ""         # saves the class to scrape...for now, we're only scraping classes
    count = 0        # saves the number of results
    results = ""     # saves the output of the scrape

    def __init__(self, website):
        self.open_page(website)
        self.always_do_these()
        self.additional_options()

    def always_do_these(self):
        """
        This method is really just an extension of __init__

        It calls the methods that will always apply when this program is run
        :return:
        """
        data_attr = self.get_attr()
        self.scrape_class(data_attr)
        self.results = self.beautiful_scrape()
        self.print_results(self.results)

    def additional_options(self):
        """
        These are the optional methods that may or may not apply when the program is run,
        plus a method used to exit the program.
        :return:
        """
        answer = 200

        while answer:
            print("\n\nPlease choose from the following options: ")
            print("Quit program:                                              0")
            print("Write results to text file:                                1")
            print("Write results to CSV:                                      2")
            print("Read joke about Soviet Russia:                             3")
            print("View the first few terms of the Fibonacci Sequence:        4")

            try:
                answer = int(input())
            except ValueError:
                print("Input not valid")
                answer = 200
            except TypeError:
                print("Input not valid")
                answer = 200
            finally:
                if answer not in [0, 1, 2, 3, 4]:
                    print("Input not valid")
                    answer = 200
                    continue

            self.go_to_method(answer)

    def go_to_method(self, answer):
        """
        This is called within additional_options().

        Its sole purpose is to take the input and call the appropriate method
        :param answer: int
        :return:
        """
        if answer == 0:
            self.exit_program()
        elif answer == 1:
            self.txt_file()
        elif answer == 2:
            self.csv_file()
        elif answer == 3:
            self.soviet_joke()
        else:
            self.fibonacci()

    def exit_program(self):
        """
        Exits gracefully
        :return:
        """
        print("Goodbye!")
        time.sleep(1)
        sys.exit(0)

    def txt_file(self):
        """
        Initiates a TextOutput object
        and uses its write_to_text_file() method
        to create a .txt of the data
        :return:
        """
        file = TextOutput()
        file.write_to_txt_file(self.results)

    def csv_file(self):
        """
        Initiates a CSVOutput object
        and uses its write_to_csv_file() method
        to create a .csv of the data
        :return:
        """
        file = CSVOutput()
        file.write_to_csv_file(self.results)

    def soviet_joke(self):
        """
        This method is just comic relief.
        It can be safely removed with no consequences to the rest of the program.
        (Just be sure to update the additional_options() method an the go_to_method()
        method accordingly)
        :return:
        """
        print("\nA Soviet judge walks out of his chambers.")
        print("He can be heard laughing uproariously.")
        print("A colleague sees him and asks, \"What's so funny?\"")
        print("\n\"I've just heard the greatest joke!\" he answers.")
        time.sleep(1)
        print("\nA bit of time passes...")
        for i in range(2):
            for i in range(3):
                time.sleep(0.5)
                print(".", end="")
            print()
        print("\n\"Well?\" asks the colleague, \"What was the joke?!\"")
        print("\nThe judge thinks for a second and answers, \"Oh, it would be imprudent to say.")
        print("I just gave the gentleman in my courtroom ten years of hard labor for telling it!\"\n")

    def fibonacci(self, a=0, b=1, i=0, terms=10):
        """
        Fibonacci sequences are fun!
        :param a: int current value
        :param b: int next value
        :param i: int current iteration
        :param terms: int number of iterations
        :return:
        """
        if i == 0:
            print("How many terms of the sequence would you like to see?")
            try:
                terms = int(input())
                if terms < 0:
                    print("Invalid number of terms.")
                    terms = 10
                    print("Number of terms has been set to 10")
            except:
                print("Invalid input")
                print("Number of terms has been set to 10")
                terms = 10
        if i == terms - 1:
            print("\nFinal term: {:,}".format(a))
            return
        if i == terms - 2:
            print("{:,}".format(a))
        elif i % 10 == 0:
            print("\n{:,}".format(a), end="; ")
        else:
            print("{:,}".format(a), end="; ")
        c = a + b
        a = b
        b = c
        i += 1
        return self.fibonacci(a, b, i, terms)

    def cycle_through_results(self):
        """
        prints scraped data
        :return:
        """
        print("\n\n")
        i = 0
        for result in self.results:
            i += 1
            print(f"Result #{i}: {result.get_text()}\n")

    def open_page(self, website):
        """

        :param website: str URL
        :return:
        """
        try:
            self.page = requests.get(website)
        except Exception as ex:
            print("Something went wrong: ")
            print(ex)
            print("The program will now exit. Goodbye!")
            self.exit_program()


    def get_attr():
        """
        selects id/element/class
        """
        choices = {1: "", 2: "class_=", 3: "id="}
        valid = False
        while not valid:
            print("\nHow would you like to search the page?")
            print("Search by element:       1")
            print("Search by class:         2")
            print("Search by id:            3")
            
            try:
                choice = int(input("Please enter the number that corresponds to your choice: "))
            except:
                print("Invalid choice.\n")
                choice = 0
                
            valid = choice in choices
                
        return choices[choice]
    
    
    def scrape_class(self, data_attr):
        """
        This is really just getting the HTML 
        element, id, or class to scrape.
        :return:
        """
        print(f"Please enter {data_attr} to scrape: ")
        self.cls = input()
        

    def beautiful_scrape(self, data_attr):
        """
        parses HTML of site
        creates a list of results
        saves results to self.results
        and returns results (they're currently never used,
        but they may be in the future)
        :return:
        """
        soup = BeautifulSoup(self.page.content, "html.parser")
        resulting_text = soup.find_all(data_attr + self.cls)
        self.results = resulting_text
        return resulting_text

    def print_results(self, results):
        """
        prints the number of results and calls cycle_through_results()
        :param results: list of scraped results
        :return:
        """
        self.count = len(results)
        print(f"NUMBER OF RESULTS: {self.count}")
        self.cycle_through_results()

#
# This class outputs the results to a CSV
# It has undergone limited testing,
# so please feel free to break it and
# let me know what needs to be updated
#
class CSVOutput:
    direction = -1
    filename = ""

    def __init__(self):
        self.get_filename()
        self.check_filename()
        self.get_direction()

    def get_filename(self):
        """
        gets filename from user
        :return:
        """
        self.filename = input("Please enter the name of the file you would like to write: ")

    def check_filename(self):
        """
        adds .csv to filename if it does not yet exist
        :return:
        """
        if self.filename[-4:] != ".csv":
            self.filename += ".csv"

    def get_direction(self):
        """
        Determines whether to print a column or a row of data
        :return:
        """
        valid = False

        while not valid:
            print("Please choose one of the following directions: ")
            print("1 for vertical. Your data would look like this on a spreadsheet: "\
                  "\ndata\ndata\ndata")
            print("2 for horizontal. Your data would look like this on a spreadsheet: "\
                  "data, data, data")

            try:
                self.direction = int(input())
            except ValueError:
                print("Invalid input")
            except TypeError:
                print("Invalid input")
            except: # yes, I know that pep8 doesn't like this
                print("Invalid input")
            finally:
                if self.direction not in [1, 2]:
                    print("Invalid input.")
                else:
                    valid = True

    def write_to_csv_file(self, results):
        """
        Writes csv to current directory
        :param results: list of data
        :return:
        """
        try:
            full_path = "./" + self.filename
            with open(full_path, "w") as csv_file:
                for result in results:
                    if self.direction == 1:
                        result = result.get_text().strip()
                        result = result.replace("\n", "")
                        csv_file.write(result + "\n")
                    else:
                        result = result.get_text().strip()
                        result = result.replace("\n", "")
                        csv_file.write(result + ",")
        except:
            print("Something went wrong. Please try again.")
            sys.exit(1)
        print("File written successfully in location: " + os.curdir)

#
# Exports data to text file
# Like the CSVOutput class,
# this class has undergone very little testing
#
class TextOutput:
    filename = ""

    def __init__(self):
        self.get_filename()
        self.check_filename()

    def get_filename(self):
        """
        gets filename from user
        :return:
        """
        self.filename = input("Please enter the name of the file you would like to write: ")

    def check_filename(self):
        """
        adds .txt extension to file if it does not yet exist
        :return:
        """
        if self.filename[-4:] != ".txt":
            self.filename += ".txt"

    def write_to_txt_file(self, results):
        """
        exports data to .txt in current directory
        :param results: list of data
        :return:
        """
        try:
            full_path = "./" + self.filename
            with open(full_path, "w") as txt_file:
                for result in results:
                    result = result.get_text().strip()
                    result = result.replace("\n", "")
                    txt_file.write(result + "\n")
        except Exception as e:
            print(e)
            print("Something went wrong. Please try again.")
            sys.exit(1)
        print("File written successfully in location: " + os.curdir)


#
# spoiler: __name__ DOES == '__main__'!!!!!!!!!!!!!11111omgomgomgOMGOMGOMG
#
# This is a rather silly convention, isn't it?
#
if __name__ == '__main__':
    site = input("Please enter URL to scrape: ") # This is my only global(ish). Gets URL from user
    Pagedata(site) # <-- The magic and the madness happen here
    # Here's a comment just to annoy pep8 dictators ;-)
