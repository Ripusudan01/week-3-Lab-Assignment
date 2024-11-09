import sys, csv
from jinja2 import Template
import matplotlib.pyplot as plt

with open("data.csv", newline= '') as csvfiles:
     reader = csv.reader(csvfiles)
     student_course = []
     course_mark = []
# print(reader)


     input_list = sys.argv

     total_me = 0
     if input_list[1] == '-s':
          for row in reader:
               if input_list[2] in row[0]:
                    total_me += int(row[2].strip())
                    student_course.append(row)
          if student_course == []:
               data = """
               <!DOCTYPE html>
               <html lang="en">
               <head>
               <meta charset="UTF-8">
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Something Went Wrong</title>
               </head>
               <h1> Wrong Inputs </h1>
               <p> Something went wrong </p>
               </html>
               """
               file = open('output.html', 'w') 
               file.write(data)
               file.close()
          else:
               text = """
               <!DOCTYPE html>
               <html lang="en">
               <head>
               <meta charset="UTF-8">
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Student Data</title>
               </head>
               <body>
               <h1>Student Details</h1>
               <table border="1">
                    <thead>
                         <tr>
                              <th>Student ID</th>
                              <th>Course ID</th>
                              <th>Marks</th>
                         </tr>
                    </thead>
                    <tbody>
                         {% for student in student_course %}
                         <tr>
                              <td>{{ student[0].strip() }}</td>
                              <td>{{ student[1].strip() }}</td>
                              <td>{{ student[2].strip() }}</td>
                         </tr>
                         {% endfor %}
                    </tbody>
               <thead>
               <tr>
                    <td colspan="2"><strong>Total Marks</strong></td>
                    <td>{{ total }}</td>
               </tr>
               </thead>
               </table>
               </body>
               </html>"""   
               temp = Template(text) 
               output1 = temp.render(total = total_me, student_course = student_course)
               File = open('output.html','w')
               File.write(output1)
               File.close()
     elif input_list[1] == '-c':
          for row in reader:
               if input_list[2] in row[1]:
                    course_mark.append(int(row[2].strip()))
          if course_mark == []:
               data = """
               <!DOCTYPE html>
               <html lang="en">
               <head>
               <meta charset="UTF-8">
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Something Went Wrong</title>
               </head>
               <h1> Wrong Inputs </h1>
               <p> Something went wrong </p>
               </html>
               """
               file = open('output.html', 'w') 
               file.write(data)
               file.close()
          else:
               average_mark = sum(course_mark)/len(course_mark)
               maximum_mark = max(course_mark)

               course_data = """
               <!DOCTYPE html>
               <html lang="en">
               <head>
               <meta charset="UTF-8">
               <meta name="viewport" content="width=device-width, initial-scale=1.0">
               <title>Course Data</title>
               </head>
               <h1> Course Details </h1>
               <table border = "1"> 
                    <tr>
                         <th> Average Marks </th>
                         <th> Maximum Marks </th>
                    </tr>
                    <tr>
                         <td> {{average_mark}} </td>
                         <td> {{maximum_mark}} </td>
                    </tr>

               </table>
               <img src="hist.png" alt="histogram.img">
               </html>
               """ 
               temp = Template(course_data)
               output = temp.render(average_mark = average_mark, maximum_mark = maximum_mark)

               x = course_mark
               plt.hist(x)
               plt.savefig("hist.png")

               File = open("output.html","w")
               File.write(output)
               File.close()
