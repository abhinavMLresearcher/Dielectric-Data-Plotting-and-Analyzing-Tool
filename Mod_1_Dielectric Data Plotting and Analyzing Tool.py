import tkinter
from tkinter import ttk
from tkinter import messagebox
import numpy as np
# creating  numpy array

import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

# Import required libraries
from tkinter import *
from tkinter import filedialog
from tkinter import ttk


# Import required libraries
from tkinter import *
from tkinter import ttk
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import math


Temp_fre1=["Temp(oC)","Freq(Hz)"]
axis_array=["x", "frequency", "dielctr", "tan"]
X_axis=["Freq(Hz)","Temp(oC)"]

X_axis_plot1=[["Freq(Hz)","Temp(oC)"],["Temp(oC)","Freq(Hz)"]]
header_parameters=["Freq(Hz)","Temp(oC)", "Capacitance(F)", "tan(delta)","Mod Z(ohm)","Real E", "Img E", "Mod E", "Real Z(ohm-m)", "Img Z(ohm-m)", "Mod Z(ohm-m)", "Real M ", "Img M", "Mod M", "Real Y(ohm-1)", "Img Y(ohm-1)", "Mod Y(ohm-1)","Conductivity(Sm-1)"]
header_parameters_freq=["Freq(Hz)","Temp(oC)", "Capacitance(F)", "tan(delta)","Mod Z(ohm)","Real E", "Img E", "Mod E", "Real Z(ohm-m)", "Img Z(ohm-m)", "Mod Z(ohm-m)", "Real M ", "Img M", "Mod M", "Real Y(ohm-1)", "Img Y(ohm-1)", "Mod Y(ohm-1)","Conductivity(Sm-1)"]
header_parameters_temp=["Temp","Freq", "Capacitance(F)", "tan(delta)","Mod Z(ohm)","Real E", "Img E", "Mod E", "Real Z(ohm-m)", "Img Z(ohm-m)", "Mod Z(ohm-m)", "Real M ", "Img M", "Mod M", "Real Y(ohm-1)", "Img Y(ohm-1)", "Mod Y(ohm-1)","Conductivity(Sm-1)"]

header_parameters_freq_temp=[header_parameters_freq, header_parameters_temp ]

headre_unit=["Hz", "oC", "F", " ","Ohm"," ", " "," ", "Ohm-m", "Ohm-m" , "Ohm-m"," ","","","Ohm-1","Ohm-1","Ohm-1","S/m"]
headre_unit_freq=["Hz", "oC", "F", " ","Ohm"," ", " "," ", "Ohm-m", "Ohm-m" , "Ohm-m"," ","","","Ohm-1","Ohm-1","Ohm-1","S/m"]
headre_unit_temp=["oC", "Hz", "F", " ","Ohm"," ", " "," ", "Ohm-m", "Ohm-m" , "Ohm-m"," ","","","Ohm-1","Ohm-1","Ohm-1","Sm-1"]
headre_unit_both=[headre_unit_freq,headre_unit_temp]
axis_type=["linear", "logerthmic"]

def enter_data():
    accepted = accept_var.get()

    if accepted=="Accepted":






        # User information
        Input_the_text_location = text_location_entry.get()

        Thickness1 = thickness_entry.get()
        Diemeter1 = area_entry.get()

        Sample_name=sample_entry.get()

        Digit_thickness1 = Thickness1.replace('.','',1).isdigit()
        Digit_Diemeter1 =  Diemeter1.replace('.','',1).isdigit()





        if Input_the_text_location and Digit_thickness1==True and Digit_Diemeter1==True and Sample_name :
             # Input paramter information

            Thickness = float(thickness_entry.get())
            Diemeter = float(area_entry.get())

            if Thickness ==0 or  Diemeter ==0:
                tkinter.messagebox.showwarning(title="Error", message=" 0 is not allowed ")


            else:
                all_outfile_confirmation = all_output_var.get()

                scale_value1=s.get()
                scale_value2=s1.get()

                scale_value11=s_cc.get()
                scale_value21=s_cc1.get()

                scale_value12=s_cc12.get()
                scale_value22=s_cc2.get()






                print("all_outfile_confirmation", all_outfile_confirmation)

                #two_axis_outfile_confirmation=axis_2_data_output_var.get()
                #print("axis_2_data__confirmation", two_axis_outfile_confirmation)


                three_axis_outfile_confirmation=axis_3_data_output_var.get()


                print("axis_3_data__confirmation", three_axis_outfile_confirmation)


                three_axis_outfile_confirmation_plot=axis_3_data_output_var_plot.get()


                print("axis_3_data__confirmation_plot", three_axis_outfile_confirmation_plot)

                # First row
                #X1_two_outfile=X1_combobox.get()
                #X1_two_outfile_index=X_axis.index( X1_two_outfile)
                #print(" X1_two_outfile=X1_combobox", X1_two_outfile_index)

                #Y1_two_outfile=Y1_combobox.get()
                #Y1_two_outfile_index=header_parameters.index( Y1_two_outfile)
                #print(" Y1_two_outfile=X1_combobox", Y1_two_outfile_index)
                #second row
                X2_two_outfile=X2_combobox.get()
                X2_two_outfile_index=X_axis.index( X2_two_outfile)
                print(" X2_two_outfile=X1_combobox", X2_two_outfile_index)

                Y2_two_outfile=Y2_combobox.get()
                Y2_two_outfile_index=header_parameters.index( Y2_two_outfile)
                print(" Y1_two_outfile=X1_combobox", Y2_two_outfile_index)

                Z2_two_outfile=Z2_combobox.get()
                Z2_two_outfile_index=header_parameters.index( Z2_two_outfile)
                print(" Z2_two_outfile_index_plot", Z2_two_outfile_index)

                #Ploting row
                X2_two_outfile_plot=X2_combobox_plot.get()
                X2_two_outfile_index_plot=X_axis.index( X2_two_outfile_plot)
                print(" X2_two_outfile=X1_combobox_plot", X2_two_outfile_index_plot)

                Y2_two_outfile_plot=Y2_combobox_plot.get()
                Y2_two_outfile_index_plot=header_parameters.index( Y2_two_outfile_plot)
                print(" Y1_two_outfile=X1_combobox_plot", Y2_two_outfile_index_plot)

                Z2_two_outfile_plot=Z2_combobox_plot.get()
                Z2_two_outfile_index_plot=header_parameters.index( Z2_two_outfile_plot)
                #print(" Z2_two_outfile_index_plot", Z2_two_outfile_index_plot)



                selected_axis_type=Z2_combobox_plot1.get()
                selected_axis_type_index=axis_type.index(selected_axis_type)

                selected_axis_type2=Z2_combobox_plot2.get()
                selected_axis_type_index2=axis_type.index(selected_axis_type2)





                import numpy as np



                # finding input path loacton in the python style
                print("Input_the_text_location: ",Input_the_text_location)
                location_string=str(Input_the_text_location)
                rpl1=location_string.replace("\\", "/")
                rpl2=rpl1.replace('"','')
                directory_location_in_python=str(rpl2)
                print("directory_location_in_python", directory_location_in_python)

                import logging

                try:
                # Getting_input filein the matrix using from path location
                    input_data=np.loadtxt(f"{directory_location_in_python}", skiprows=1, encoding = 'unicode_escape', dtype=str)

                    #num1=[["1","2.5699999999 K","3"],["1","2 M","3"],["1","2 n","8"],["1","2 M","3"]]



                    num2=input_data
                    input_index=np.shape(num2)   #except header

                    print("index", input_index)

                    print(type(num2))

                    units={"K":10**3,"M":10**6,"p":10**-12, "n":10**-9, "m":10**-3, "G":10**9, "u":10**-6}  # make a dict that contain the value that they represent
                    result1=[]
                    for j in range(0,input_index[0]):


                        k=int(j)
                        for n in num2[k]:
                             try:
                                 result1.append( float(n) )  #try to comber it to a number
                             except ValueError:

                                #str(n).replace(" ",'')
                                #k.append(n)

                                unit=n[-1]                 #get the letter
                                n = float( n[:-1] )        #convert all but the letter
                                P=result1.append( n * units[unit] )
                    print(result1)

                    mat1 = []
                    while result1 != []:
                      mat1.append(result1[:input_index[1]])
                      result1 = result1[input_index[1]:]
                    print(mat1)
                    input_data=np.array(mat1)




                except Exception as e:
                    logging.warning(e)
                    logging.error(e)
                    tkinter.messagebox.showwarning(title="Error", message="All cell values are not number !! \n Its reason may be spacing between number and string (example n,p,K etc), O/R or blank etc \n check out")



                #Digit_input_data  = np.char.isdigit(input_data)



                #print("input_data is +", input_data)


                tran_input_data=np.transpose(input_data)
                print("input_data is shaoe+", input_data.shape)
                print("input_data is shaoe+", tran_input_data)
                print("input_data is shaoe+", type(tran_input_data))

                row_colomn_input1=input_data.shape    # no of row and colomn of the input text file

                if row_colomn_input1[1]==5:

                    # Here new colomne i.e realz, imag Z.... will be added using the formula

                    Z_unit=Thickness/(math.pi*Diemeter*Diemeter*1E-3)

                    Z_unit_multification_factor=1/Z_unit
                    print(Z_unit)
                    Eo_constant=4*Thickness/(math.pi*Diemeter*Diemeter*8.85E-15)
                    Eo_constant_multification_factor=1/Eo_constant
                    print(Eo_constant)







                    new_colomn_Real_E=tran_input_data[3]*Eo_constant

                    print(new_colomn_Real_E)


                    new_colomn_Img_E=tran_input_data[3]*tran_input_data[2]*Eo_constant
                    new_colomn_Mod_E=np.sqrt( new_colomn_Real_E* new_colomn_Real_E+new_colomn_Img_E*new_colomn_Img_E)

                    print(new_colomn_Img_E)

                    new_colomn_Mod_Z=tran_input_data[4]*Z_unit_multification_factor
                    new_colomn_Real_Z=new_colomn_Mod_Z* np.sin(np.arctan((tran_input_data[2])))
                    new_colomn_Img_Z=new_colomn_Mod_Z* np.cos(np.arctan((tran_input_data[2])))



                    new_colomn_Real_M= 2*math.pi*tran_input_data[0]*new_colomn_Img_Z*Z_unit*Eo_constant_multification_factor
                    new_colomn_Img_M=2*math.pi*tran_input_data[0]*new_colomn_Real_Z*Z_unit*Eo_constant_multification_factor
                    new_colomn_Mod_M=np.sqrt( new_colomn_Real_M* new_colomn_Real_M+new_colomn_Img_M*new_colomn_Img_M)

                    new_colomn_Real_Y  =2*math.pi*tran_input_data[0]*new_colomn_Img_E*Z_unit*Eo_constant_multification_factor
                    new_colomn_Img_Y=2*math.pi*tran_input_data[0]*new_colomn_Real_E*Z_unit*Eo_constant_multification_factor
                    new_colomn_Mod_Y=np.sqrt( new_colomn_Real_Y* new_colomn_Real_Y+new_colomn_Img_Y*new_colomn_Img_Y)

                    new_colomn_conductivity=new_colomn_Real_E *tran_input_data[2]*tran_input_data[0]*2*math.pi*8.85E-12

                    M_5= np.matrix(new_colomn_Real_E)
                    M_6=np.matrix(new_colomn_Img_E)
                    M_7=np.matrix(new_colomn_Mod_E)
                    M_8=np.matrix(new_colomn_Real_Z)
                    M_9=np.matrix(new_colomn_Img_Z)
                    M_10=np.matrix(new_colomn_Mod_Z)
                    M_11=np.matrix(new_colomn_Real_M)
                    M_12=np.matrix(new_colomn_Img_M)
                    M_13=np.matrix(new_colomn_Mod_M)
                    M_14=np.matrix(new_colomn_Real_Y)
                    M_15=np.matrix(new_colomn_Img_Y)
                    M_16=np.matrix(new_colomn_Mod_Y)
                    M_17=np.matrix(new_colomn_conductivity)

                    modified_tran_input=tran_input_data

                    M_0_4=np.matrix(modified_tran_input)

                    #final_hedare = header.concatenate((mat_x22, mat_x21,matrix_header_3_row), axis = 0)

                    M0_17=np.concatenate((M_0_4, M_5,M_6,M_7,M_8,M_9,M_10,M_11,M_12,M_13,M_14,M_15,M_16,M_17), axis=0)

                    print("M0_17", M0_17 )

                    trans_M0_17=np.transpose(M0_17)
                    array_trans_M0_17=np.array(trans_M0_17)


                    #np.savetxt('modified_input1245.txt', M0_17, delimiter='  ', fmt="%s\t")





                    #sortening the modified input data Temperature and freqency


                    #ordereing the data_as per temperat colmon getting input file
                    #Frequence

                    array_input1=np.array(array_trans_M0_17)
                    a=array_input1
                    #a = ([[1, 10, 3],  [3, 10, 7],[1, 20, 3], [2, 20, 7], [3, 40, 7], [3, 20, 7], [2, 10, 6],  [2, 30, 7], [3, 30, 7], [1, 40, 7], [1, 30, 7], [2, 40, 7]]);
                    a1 = sorted(a, key=lambda a_: a_[0])
                    print("ordere1",a1)
                    b = sorted(a1, key=lambda a1_: a1_[1])
                    print("ordere",b)


                    # data in ascending ordre
                    c= sorted(b, key=lambda b_:b_[1])
                    print("Frequency_points_input",c)
                    m5=np.matrix(c)
                    #np.savetxt('fre_points.txt', c, delimiter='  ', fmt="%s\t")

                    d= sorted(c, key=lambda b_: b_[0])
                    print("tempe_points",d)
                    e=np.transpose(d)
                    f=np.matrix(e)
                    f[[1, 0]] = f[[0, 1]]
                    g=np.transpose(f)
                    print("stempe point",g)
                    #np.savetxt('tempe_points.txt', g, delimiter='  ', fmt="%s\t")
                    m11=g

                    m12=np.matrix(m11)
                    print("temp_sort", m12)

                    M_input_array=[m5,m12] #m5 and m12 are the two fre and tempe sortening input
                    print("M_input_array", M_input_array)

                     #for writing file_output as string with cirtain decimal

                    st = array_trans_M0_17
                    st_n = np.array(["%.6f" % w for w in st.reshape(st.size)])
                    st_n = st_n.reshape(st.shape)
                    string_modified_input=np.array(st_n)
                    matrix_string_modified_input=np.matrix(string_modified_input)
                    #np.savetxt('string_modified_input.txt', string_modified_input, delimiter=' ',   fmt="%s\t")

                    import numpy as np


                    # it is for finding number of freq points

                    C1_fr=np.transpose(m5)
                    C2_fr=np.array(C1_fr[1][0])   # it will take data
                    C3_fr=C2_fr[0]   #it decide counting value
                    C4_fr=C3_fr[0]
                    print("count",C4_fr) # value which is counted
                    C5_fr = C3_fr.tolist()   # converting array to list
                    print("list",C5_fr)
                    C6_fr=C5_fr.count(C4_fr)
                    print("number of freqiency_count",C6_fr)


                    #it is for finding number of tempe points

                    C1_temp=np.transpose(m12)
                    C2_temp=np.array(C1_temp[1][0])   # it will take data
                    C3_temp=C2_temp[0]   #it decide counting value
                    C4_temp=C3_temp[0]
                    print("count",C4_temp) # value which is counted
                    C5_temp = C3_temp.tolist()   # converting array to list
                    print("list",C5_temp)
                    C6_temp=C5_temp.count(C4_temp)
                    print("number of temp_count",C6_temp)



                    if row_colomn_input1[0]==C6_temp*C6_fr and row_colomn_input1[1]==5:
                        print("Input file is correct")
                    else:
                        tkinter.messagebox.showwarning(title="Error", message=" Input Data has some issues and specially with the number of freq and temp points")

                    freq_points=C6_fr
                    temp_points=C6_temp
                    row_points=18


                    # first threr row
                    M_swaping=[[freq_points,temp_points],
                                [temp_points,freq_points]]
                    print("M_swaping", M_swaping )

                    for i in range(0,2):
                        Sw1=i

                        # sortening will work begin from here:

                        #np.savetxt('frequenc_points.txt', M_input_array[0], delimiter=' ',   fmt="%s\t")

                        KK=M_input_array[Sw1][0:] #calling fre sorening based  and tempe-sortening based input file
                        KK1=np.array(KK)
                        print("freq_sort_from matrix",KK1 )

                        print("M_swaping[Sw1][0]",M_swaping[Sw1][0])

                        #print("matrix is acc sw", M_input_array[Sw1])


                        sort_b=KK1
                        trans_sort_b=np.transpose(sort_b)
                        slice3=M_input_array[Sw1][0:0]    # jus for giving the dimension

                        slic_fist=M_input_array[Sw1][M_swaping[Sw1][0]*0:M_swaping[Sw1][0]+M_swaping[Sw1][0]*0]
                        slic_transpos_first=np.transpose(slic_fist)

                        m123=slic_transpos_first
                        print("input_data",m123)

                        for i in range(1,M_swaping[Sw1][1]):
                            slic1=M_input_array[Sw1][M_swaping[Sw1][0]*i:M_swaping[Sw1][0]+M_swaping[Sw1][0]*i]
                            print("matrix is acc sw", slic1)
                            slic2=np.transpose(slic1)
                            m123 = np.vstack((m123, slic2))

                        input_value=np.transpose(m123)

                        print("input_data",input_value)
                        print("input_data",input_value.shape)
                        np.savetxt('input_value.txt', input_value, delimiter=' ',   fmt="%s\t")




                        #headre formation

                        hd1=header_parameters_freq_temp[Sw1]

                        hd123=header_parameters_freq_temp[Sw1]
                        for i in range(0,M_swaping[Sw1][1]-1):
                            hd2=hd1
                            hd1 = np.hstack((hd1,hd123))
                        print("parametrs_headre", hd1)
                        print("first_headre",hd1.shape)

                        # second_header

                        hd12=headre_unit_both[Sw1]
                        hd1231=headre_unit_both[Sw1]

                        for i in range(0,M_swaping[Sw1][1]-1):
                            hd22=hd12
                            hd12 = np.hstack((hd12,hd1231))
                        print("Unit parametrs_headre", hd2)

                        print("Unit parametrs_headre",hd12.shape)

                        # 3rd eader using n

                        header_3=input_value
                        m1=np.matrix(header_3)
                        print("input matrix", header_3.shape)
                        m2=m1[0]

                        m3=[]
                        for j in range(0, M_swaping[Sw1][1]):

                            for i in range(0,18):
                                m4=m2[0,j*18+1]

                                m3 = np.hstack((m3,m4))
                        print(m3)
                        print("thirda_hedaeer",m3.shape)



                        final_hedare = np.vstack((hd1, hd12))
                        final_hedare1 = np.vstack((final_hedare, m3))
                        print("final_header",final_hedare1.shape)
                        print("final_headerdd",final_hedare1)




                        pre_final_output=np.concatenate((final_hedare1, input_value), axis=0)


                        print(" pre_final_output1", pre_final_output)
                        print(" pre_final_output_shape", pre_final_output.shape)

                        trans_pre_final_output=np.transpose(pre_final_output)


                        # want to delete first colomn (1,2,3 ) from 2nd onward
                        First_del=trans_pre_final_output[0]
                        First_del1=np.matrix(First_del)
                        delet1=trans_pre_final_output
                        for i in range(0,M_swaping[Sw1][1]):
                            delet1=np.delete(delet1,18*i-i,0)

                        first_output=np.concatenate((First_del1, delet1), axis = 0)
                        trans_delete=np.transpose(first_output)
                        firts_output=trans_delete


                        print(" pre_final_output_shape", firts_output)
                        print(" first_output", firts_output.shape)



                        import os
                        import shutil
                        import numpy as np

                        N1=  Sample_name+ "_Freq_Vs_all_parameters"
                        N2=  Sample_name+ "_Temp_Vs_all_parameters"

                        folder_type=[N1,N2]

                        input_file_directory=directory_location_in_python
                        x_dr = input_file_directory.split("/")
                        x_dr.reverse()
                        x2_dr=x_dr[0]
                        x3_dr=input_file_directory.rstrip(x2_dr)
                        folder_name_slash=str(x3_dr)

                        print(folder_name_slash)





                        Output_directory=folder_name_slash
                        selected_folder=folder_type[Sw1]
                        Str_selected_folder=str(selected_folder)

                        row_1_run=all_outfile_confirmation
                        row_1_folder="Yes"

                        if row_1_run==row_1_folder:
                            print("work")


                            directory_path_all_paraters=Output_directory+Str_selected_folder

                            Str_directory_path_all_paraters=str(directory_path_all_paraters)
                            dir=Str_directory_path_all_paraters
                            A= dir
                            if os.path.exists(dir):
                                shutil.rmtree(dir)
                            os.makedirs(dir)

                            np.savetxt(f"{A}/{Sample_name}_{header_parameters_freq_temp[Sw1][0]} Vs all_parametres.txt", firts_output, delimiter=' ',   fmt="%s\t")
                            print("trans_delete", trans_delete)

                        #upto here first out_put is done.

                        #now again we well call transpose of pre_final output
                        # we will get X Y Z axis

                        trans_final_output1=np.transpose(pre_final_output)
                        first_colomn=trans_final_output1[0]
                        output_first_colomn=first_colomn

                        for j in range(0,18):
                            first_colomn23=trans_final_output1[0]
                            for i in range(0,M_swaping[Sw1][1]):

                                x123=trans_final_output1[18*i+j]
                                first_colomn23=np.insert(first_colomn23,i+1,x123,axis=0)
                            trans_output_first_colomn=np.transpose(first_colomn23)
                            print(" secenod_outputs", trans_output_first_colomn)
                            print(" first_outputs", firts_output.shape)



                            #with open(f"{header_parameters_freq_temp[Sw1][0]} Vs {header_parameters_freq_temp[Sw1][j]}.txt", 'w') as out:  # here 0 is for x axis colomn of frequenc
                            if row_1_run==row_1_folder:
                                print("work")
                                np.savetxt(f"{A}/ {Sample_name}_{header_parameters_freq_temp[Sw1][0]} Vs {header_parameters_freq_temp[Sw1][j]}.txt", trans_output_first_colomn, delimiter=' ',   fmt="%s\t")

                        #f.write({trans_output_first_colomn})
                        # upto here seprere fre, vale




                        L3Y=Y2_two_outfile_index
                        L3Z=Z2_two_outfile_index

                        L3Y_plot=Y2_two_outfile_index_plot
                        L3Z_plot=Z2_two_outfile_index_plot





                        # here we will make X axis_colomn,Z(1) and Z(2)


                        # for loop for 2nd row input








                         # here we will make X axis_colomn,Z(1) and Z(2)

                        #3nd row
                        row_3nd=three_axis_outfile_confirmation
                        print('three_axis_outfile_confirmation',three_axis_outfile_confirmation )



                        if row_3nd=="Yes":
                            row_3_sub=X2_two_outfile_index
                            first_colomn_for=trans_final_output1[0]
                            for i in range(0,M_swaping[Sw1][1]):
                                    X123=trans_final_output1[18*i+L3Y]
                                    first_colomn_for=np.insert(first_colomn_for,i+1,X123,axis=0)
                                    trans_output_first_colomn12=np.transpose(first_colomn_for)
                                    #print("seprate colomns is X3",  X123)
                            print("for X and X axis Out_put 2",  trans_output_first_colomn12)

                            if  row_3_sub==Sw1:
                                for j in range(0,M_swaping[Sw1][1]):
                                    Y123=trans_final_output1[18*j+L3Z]


                                    first_colomn_for=np.insert(first_colomn_for,2*(j+1),Y123,axis=0)
                                    trans_output_first_colomn123=np.transpose(first_colomn_for)
                                    #print("Output_X_Y_Z",  trans_output_first_colomn123)

                                    # cutting the data
                                trans_output_first_colomn123_skipped_header=  trans_output_first_colomn123[3:]

                                Trans_skipped_headre=np.transpose(trans_output_first_colomn123_skipped_header)


                                Trans_skipped_headre_skipped_first_colomn=Trans_skipped_headre[1:]
                                First_colomn_with_skipped_other=Trans_skipped_headre[0]
                                input_wihoud_header_first_colomn=np.transpose(Trans_skipped_headre_skipped_first_colomn)


                                input_wihoud_header_first_colomn_index=np.shape(input_wihoud_header_first_colomn)
                                skipping_initial_row=scale_value12
                                K111_I=(input_wihoud_header_first_colomn_index[0])*skipping_initial_row/10
                                print("trans_output_first_colomn123_index",input_wihoud_header_first_colomn_index)

                                K111_I_int=int(K111_I)

                                skipping_last_row=scale_value22
                                K111_L=(input_wihoud_header_first_colomn_index[0])*skipping_last_row/10

                                K111_L_int=int(K111_L)



                                slice_input_wihoud_header_first_colomn=input_wihoud_header_first_colomn[K111_I_int:K111_L_int]
                                First_colomn_with_skipped_other1=np.transpose(Trans_skipped_headre[0])
                                First_colomn_with_skipped_other2=First_colomn_with_skipped_other1[K111_I_int:K111_L_int]
                                First_colomn_with_skipped_other3=np.transpose(First_colomn_with_skipped_other2)
                                transpose_slice_input_wihoud_header_first_colomn=np.transpose(slice_input_wihoud_header_first_colomn)

                                slice_name_textfile=trans_output_first_colomn123[2]
                                slice_name_textfile_list = slice_name_textfile.tolist()

                                directory_path_all_paraters1=Output_directory+ Sample_name+ "_"+"Cole_Cole_"+header_parameters_freq_temp[Sw1][0]+"_"+header_parameters_freq_temp[Sw1][L3Y]+"_"+header_parameters_freq_temp[0][L3Z]

                                Str_directory_path_all_paraters1=str(directory_path_all_paraters1)
                                dir1=Str_directory_path_all_paraters1
                                B_dir= dir1
                                if os.path.exists(dir1):
                                    shutil.rmtree(dir1)
                                os.makedirs(dir1)
                                print("B",B_dir)

                                interval=2

                                skipping_initial_row1=scale_value11
                                K111_I1=(input_wihoud_header_first_colomn_index[1])*skipping_initial_row1/20



                                K111_I1_int=int(K111_I1)

                                K11_I1_even=2*K111_I1_int

                                skipping_last_row1=scale_value21
                                K111_L1=(input_wihoud_header_first_colomn_index[1])*skipping_last_row1/10

                                K111_L1_int=int(K111_L1)

                                K11_L1_even=K111_L1_int

                                print(" K11_L1_even",  K11_I1_even)
                                for i in range(K11_I1_even, K11_L1_even,2):

                                    A=transpose_slice_input_wihoud_header_first_colomn[i]
                                    B=transpose_slice_input_wihoud_header_first_colomn[i+1]
                                    C=First_colomn_with_skipped_other3[0]

                                    print("C",C)
                                    print("B",B)
                                    C_transpose=np.transpose(C)
                                    D=np.concatenate((A,B,C), axis=0)
                                    E=np.transpose(D)
                                    F=np.shape(E)   #except header
                                    print("ABC",E)

                                    G=[[F[0],"",""]]
                                    D=np.concatenate((G,E), axis=0)
                                    print("D",D)
                                    trans_slice_name_textfile=np.transpose(slice_name_textfile)
                                    H=slice_name_textfile_list[0][i+1]
                                    print("H",H)

                             # some issure are with the text file name

                                    Unit_cole_cole=[' oC', ' Hz']

                                    np.savetxt(f"{B_dir}/{H}{Unit_cole_cole[X2_two_outfile_index]} .txt", D, delimiter=' ',   fmt="%s\t")
                                    print("trans_delete", trans_delete)



                                    np.savetxt(f"{folder_name_slash} {Sample_name}_{header_parameters_freq_temp[Sw1][0]} Vs {header_parameters_freq_temp[Sw1][L3Y]} Vs {header_parameters_freq_temp[0][L3Z]}.txt", transpose_slice_input_wihoud_header_first_colomn, delimiter=' ',   fmt="%s\t")








                                    np.savetxt(f"{B_dir}/{Sample_name}_{header_parameters_freq_temp[Sw1][0]} Vs {header_parameters_freq_temp[Sw1][L3Y]} Vs {header_parameters_freq_temp[0][L3Z]}.txt", trans_output_first_colomn123, delimiter=' ',   fmt="%s\t")







                        #plotting in 4th row
                        ploting_input=input_value
                        transpose_ploting_input=np.transpose(ploting_input)
                        row_3nd_plot=three_axis_outfile_confirmation_plot
                        if row_3nd_plot=="Yes":
                            header_parameters_freq_temp1=[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],[1,0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]]
                            L3Y_plot1=header_parameters_freq_temp1[Sw1][Y2_two_outfile_index_plot]
                            L3Z_plot1=header_parameters_freq_temp1[Sw1][Z2_two_outfile_index_plot]

                            if X2_two_outfile_plot!=X_axis[Sw1]:
                                plt.clf()
                                first_colomn_for1=transpose_ploting_input[0]

                                for i in range(0,M_swaping[1][Sw1]):
                                        X123=transpose_ploting_input[18*i+L3Y_plot1]
                                        first_colomn_for1=np.insert(first_colomn_for1,i+1,X123,axis=0)
                                        trans_output_first_colomn12=np.transpose(first_colomn_for1)

                                        #m123 = np.vstack((m123, slic2))

                                        #print("trans_output_first_colomn12",  trans_output_first_colomn12)
                                slice_input_plot1_list=first_colomn_for1[1:]

                                trans_slice_input_plot1_list= slice_input_plot1_list.tolist()  # X Axis
                                print("trans_slice_input_plot1_list",  trans_slice_input_plot1_list)



                                #Y,axis_plot

                                row_3_sub=X2_two_outfile_index
                                first_colomn_for2=transpose_ploting_input[0]

                                M_initial=[]
                                print('initial',M_initial)

                                for i in range(0,M_swaping[Sw1][1]):
                                    X123=transpose_ploting_input[18*i+L3Z_plot1]
                                    first_colomn_for2=np.insert(first_colomn_for2,i+1,X123,axis=0)
                                    trans_output_first_colomn12=np.transpose(first_colomn_for2)
                                    m4=m3[i*18+1]

                                    M_initial = np.hstack((M_initial, m4))

                                print("Lable__",M_initial)

                                    #m3_123=Label[18*i+0]
                                    #Label=np.insert(Label, i+1, m3_123)

                                #print("Label_new", Label)
                                print("trans_output_first_colomn12",  trans_output_first_colomn12)
                                slice_input_plot2_list=first_colomn_for2[1:]

                                trans_slice_input_plot2_list= slice_input_plot2_list.tolist()  # Y Axis


                                    #print("seprate colomns is X3",  X123)





                                lable_plot= first_colomn_for2[0][0]
                                print('lebal',lable_plot )



                                #Label_Y=Y_axis_for_multiple_YY[2]
                                Label_list=lable_plot.tolist()



                                Label_list_value=Label_list[0]
                                print("Label_list",Label_list_value)


                                X12=trans_slice_input_plot1_list

                                Y12=trans_slice_input_plot2_list



                                Matrix_size=slice_input_plot2_list.shape
                                print("Matrix_size",Matrix_size)

                                #np.savetxt("slice_input_plot2.txt",   trans_output_first_colomn1, delimiter=' ',   fmt="%s\t")
                                #np.savetxt("slice_input_plot1.txt",  trans_output_first_colomn12, delimiter1=' ',   fmt="%s\t")
                                range1= Matrix_size[0]*scale_value1/10
                                print(range1)
                                int_range1=int( range1)
                                range2= Matrix_size[0]*scale_value2/10
                                int_range2=int( range2)

                                print(int_range2)
                                print(int_range1)
                                for i in range(int_range1,int_range2):
                                    X_axis_plot=[[' oC', ' Hz'],[' Hz', ' Oc']]
                                    b=str(X_axis_plot[Sw1][0])
                                    lable_1=str( M_initial[i])
                                    lable_=lable_1+ b

                                    #print("abel_list",  lable_plot_value)

                                    X123=[X12][0][i]
                                    Y123=[Y12][0][i]

                                    X1=X123

                                    Y1=Y123

                                    Z1=[X1,Y1]

                                    Tra_Z1=np.transpose(Z1)
                                    Sort_tranZ1= sorted(Tra_Z1, key=lambda b_: b_[0])

                                    trans_Sort_tranZ1=np.transpose(Sort_tranZ1)

                                    trans_Sort_tranZ1_value_x=trans_Sort_tranZ1[0]
                                    trans_Sort_tranZ1_value_y=trans_Sort_tranZ1[1]



                                    #Label_list1=Label_list[0][i]


                                    plt.plot(trans_Sort_tranZ1_value_x, trans_Sort_tranZ1_value_y, label=lable_,marker="*", markersize=10)














                                plt.title(f"{X_axis_plot1[Sw1][1]}_{header_parameters_freq[L3Y_plot]} VS {header_parameters_freq[L3Z_plot]}", loc = 'right', fontweight='bold',fontsize=14, color="red")
                                plt.xlabel(f"{header_parameters_freq[L3Y_plot]}", fontweight='bold',fontsize=14,color="black")
                                plt.ylabel(f"{header_parameters_freq[L3Z_plot]}",fontweight='bold', fontsize=14,color="blue" )



                                #plt.set_xlabel('X-axis ')
                                #plt.set_ylabel('Y-axis ')

                                #plt.xaxis.label.set_color('yellow')        #setting up X-axis label color to yellow
                                #plt.yaxis.label.set_color('blue')          #setting up Y-axis label color to blue

                                plt.tick_params(axis='x', colors='black', labelsize=13)    #setting up X-axis tick color to red
                                plt.tick_params(axis='y', colors='blue',labelsize=13)  #setting up Y-axis tick color to black

                                #plt.spines['left'].set_color('red')        # setting up Y-axis tick color to red
                                #plt.spines['top'].set_color('red')         #setting up above X-axis tick color to red

                                #label_input=input_plot[0]
                                plt.rcParams["figure.figsize"] = [300, 700]
                                plt.rcParams["figure.autolayout"] =True
                                scale_type=["linear","log"]
                                plt.xscale(scale_type[selected_axis_type_index])

                                plt.yscale(scale_type[selected_axis_type_index2])
                                #plt.xaxis.set_minor_locator(MultipleLocator(5))
                                #plt.xaxis.set_major_locator(loc)
                                #plt.style.use('dark_background')

                                #ax = plt.axes()

                                # Setting the background color of the
                                # plot using set_facecolor() method
                                #ax.set_facecolor("violet")
                                plt.grid(color='green', linestyle='--', linewidth=.7)
                                plt.legend(loc='lower right', ncol=1)
                                #ax=plt.axes()
                                #ax.set_facecolor('#C0C0C0')

                                plt.show()











                else:
                     tkinter.messagebox.showwarning(title="Error", message=" The input data has some issues related to number of colomns")
        else:
            tkinter.messagebox.showwarning(title="Error", message=" Checked the Parameters ")
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not accepted the terms")
import tkinter as tk
window = tkinter.Tk()
window.title("Dielectric Data Plotting and Analyzing Tool [Copyright@Abhinav K.,IIT Hyderabad]" )

frame = tkinter.Frame(window)
frame.configure(bg='#E0FFFF')
frame.pack()

# 0th_row_for_Paremters informations & all out files


basic_input_data =tkinter.LabelFrame(frame, text="Parameter informations", foreground="white",  bg="#A52A2A", bd=10,font=("Times New Roman",13))
basic_input_data.grid(row=0, column=0, sticky="news", padx=10, pady=5)



# Create a label widget
text_location_label = tkinter.Label(basic_input_data, text="Paste input text file location")
text_location_label.grid(row=0, column=0)
text_location_entry = tkinter.Entry(basic_input_data, width=20)
text_location_entry.grid(row=1, column=0)

thickness_label = tkinter.Label(basic_input_data, text="Thickness(mm)")
area_lebel = tkinter.Label(basic_input_data, text="Diameter(mm)")
thickness_label.grid(row=0, column=2)
area_lebel.grid(row=0, column=3)

thickness_entry = tkinter.Entry(basic_input_data, width=20)
area_entry = tkinter.Entry(basic_input_data,  width=20)
thickness_entry.grid(row=1, column=2)
area_entry.grid(row=1, column=3)

sample_label = tkinter.Label(basic_input_data, text="Sample Name")
sample_label.grid(row=0, column=5)
sample_entry = tkinter.Entry(basic_input_data, width=20)
sample_entry.grid(row=1, column=5)




for widget in basic_input_data.winfo_children():
    widget.grid_configure(padx=25, pady=5)

# for row=1 for two axis output files





#axis_2_frame =tkinter.LabelFrame(frame, text="All or specific two axises output files",bg="#5F9EA0" , foreground="white",   bd=10,font=("Times New Roman",13))
#axis_2_frame.grid(row=1, column=0,  padx=10, pady=5, sticky="news")

all_output_label = tkinter.Label(basic_input_data, text="You want all output files?" )
all_output_var = tkinter.StringVar(value="No")
all_output_check = tkinter.Checkbutton(basic_input_data, text="Yes",
                                       variable=all_output_var, onvalue="Yes", offvalue="No")
all_output_label.grid(row=0, column=6)
all_output_check.grid(row=1, column=6)






#axis_2_data_output_var = tkinter.StringVar(value="No")
#axis_2_data_output_check = tkinter.Checkbutton(axis_2_frame, text="Yes",
                                       #variable=axis_2_data_output_var, onvalue="Yes", offvalue="No")

#axis_2_data_output_label.grid(row=0, column=1)
#axis_2_data_output_check.grid(row=1, column=1)

#X1_label = tkinter.Label(axis_2_frame, text="X axis (Frequency/Temperature")

#X1_combobox = ttk.Combobox(axis_2_frame, values=X_axis , state="readonly", width=17)
#X1_combobox.current(1)

#X1_label.grid(row=0, column=2)
#X1_combobox.grid(row=1, column=2)

#Y1_label = tkinter.Label(axis_2_frame, text="Y axis")

#Y1_combobox = ttk.Combobox(axis_2_frame, values=header_parameters , state="readonly", width=17)
#Y1_combobox.current(5)

#Y1_label.grid(row=0, column=3)
#Y1_combobox.grid(row=1, column=3)
#for widget in axis_2_frame.winfo_children():
    #widget.grid_configure(padx=10, pady=5)

# row=2_for 3_axis_selected dats


axis_3_frame = tkinter.LabelFrame(frame, text="Three axes output and Cole-Cole files", foreground="white",  bg="#708090", bd=10,font=("Times New Roman",13))
axis_3_frame.grid(row=2, column=0, sticky="news", padx=10, pady=5)


axis_3_data_output_label = tkinter.Label(axis_3_frame, text="Do you need this? ")
axis_3_data_output_var = tkinter.StringVar(value="No")
axis_3_data_output_check = tkinter.Checkbutton(axis_3_frame, text="Yes",
                                       variable=axis_3_data_output_var, onvalue="Yes", offvalue="No")

axis_3_data_output_label.grid(row=0, column=0)
axis_3_data_output_check.grid(row=1, column=0)

X2_label = tkinter.Label(axis_3_frame, text="Freq (X axis)-Temp(Cole_Cole)")
X2_label.grid(row=0, column=1)
X2_combobox = ttk.Combobox(axis_3_frame, values=X_axis , state="readonly", width=17)
X2_combobox.current(1)
X2_combobox.grid(row=1, column=1)

Y2_label = tkinter.Label(axis_3_frame, text="Y axis")
Y2_combobox = ttk.Combobox(axis_3_frame, values=header_parameters , state="readonly", width=17)
Y2_combobox.current(8)
Y2_label.grid(row=0, column=2)
Y2_combobox.grid(row=1, column=2)

Z2_label = tkinter.Label(axis_3_frame, text="Z axis")
Z2_combobox = ttk.Combobox(axis_3_frame, values=header_parameters , state="readonly", width=17)
Z2_combobox.current(9)
Z2_label.grid(row=0, column=3)
Z2_combobox.grid(row=1, column=3)


for widget in axis_3_frame.winfo_children():
    widget.grid_configure(padx=50, pady=2)


# row=3_for 4_plot_axis_selected dats


axis_3_frame_plot = tkinter.LabelFrame(frame, text="Select X, Y and Z axes for plot" , foreground="white",  bg="#5F9EA0", bd=10,font=("Times New Roman",13))
axis_3_frame_plot.grid(row=3, column=0, sticky="news", padx=10, pady=5)


axis_3_data_output_label_plot = tkinter.Label(axis_3_frame_plot, text="Do you want plotting? ")
axis_3_data_output_var_plot = tkinter.StringVar(value="No")
axis_3_data_output_check_plot = tkinter.Checkbutton(axis_3_frame_plot, text="Yes",
                                       variable=axis_3_data_output_var_plot, onvalue="Yes", offvalue="No")

axis_3_data_output_label_plot.grid(row=0, column=0)
axis_3_data_output_check_plot.grid(row=1, column=0)

X2_label_plot = tkinter.Label(axis_3_frame_plot, text=" Freq/Temp curve")
X2_label_plot.grid(row=0, column=1)
X2_combobox_plot = ttk.Combobox(axis_3_frame_plot, values=X_axis , state="readonly", width=17)
X2_combobox_plot.current(0)
X2_combobox_plot.grid(row=1, column=1)

Y2_label_plot = tkinter.Label(axis_3_frame_plot, text="X axis")
Y2_combobox_plot = ttk.Combobox(axis_3_frame_plot, values=header_parameters , state="readonly", width=17)
Y2_combobox_plot.current(1)
Y2_label_plot.grid(row=0, column=2)
Y2_combobox_plot.grid(row=1, column=2)

Z2_label_plot = tkinter.Label(axis_3_frame_plot, text="Y axis")
Z2_combobox_plot = ttk.Combobox(axis_3_frame_plot, values=header_parameters , state="readonly", width=17)
Z2_combobox_plot.current(5)
Z2_label_plot.grid(row=0, column=3)
Z2_combobox_plot.grid(row=1, column=3)









#cole_cole_plot

l_cc = tkinter.Label(axis_3_frame, bg='#B03A2E', fg='white', width=20, text='0.00')
l_cc.grid(row=4, column=0, sticky="news", padx=10, pady=10)
#l.pack()

def print_selection(v):
    l_cc.config(text='' + v)

s_cc = tk.Scale(axis_3_frame, label='Initial points(colomn)', bg='#B03A2E', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s_cc.grid(row=5, column=0)


l_cc1 = tkinter.Label(axis_3_frame, bg='#B03A2E', fg='white', width=0, text='0.00')
l_cc1.grid(row=4, column=1, sticky="news", padx=10, pady=10)
#l.pack()

def print_selection(v):
    l_cc1.config(text='' + v)

s_cc1 = tk.Scale(axis_3_frame, label='Final points(colomn)', bg='#B03A2E', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s_cc1.grid(row=5, column=1)

l_cc12 = tkinter.Label(axis_3_frame, bg='#212F3C', fg='white', width=20, text='0.00')
l_cc12.grid(row=4, column=2, sticky="news", padx=10, pady=10)
#l.pack()

def print_selection(v):
    l_cc12.config(text='' + v)

s_cc12 = tk.Scale(axis_3_frame, label='Initial points(row)', bg='#212F3C', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s_cc12.grid(row=5, column=2)


l_cc2 = tkinter.Label(axis_3_frame, bg='#212F3C', fg='white', width=20, text='0.00')
l_cc2.grid(row=4, column=3, sticky="news", padx=10, pady=10)
#l.pack()

def print_selection(v):
    l_cc2.config(text='' + v)

s_cc2 = tk.Scale(axis_3_frame, label='Final points(row)', bg='#212F3C', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s_cc2.grid(row=5, column=3)




for widget in axis_3_frame_plot.winfo_children():
    widget.grid_configure(padx=10, pady=5)





# row=3 Given informations is okay (term and condiction)
terms_frame = tkinter.LabelFrame(frame, text="" , foreground="white",  bg="#708090", bd=10,font=("Times New Roman",13))
terms_frame.grid(row=5, column=0, sticky="news", padx=10, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "Given informations are okay",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)




# En row-=4 (Enter)
button = tkinter.Button(frame, text="Run the program", command= enter_data, foreground="white", bg="#B22222", bd=10,font=("Times New Roman",13))
button.grid(row=6, column=0, sticky="news", padx=10, pady=10)




#window = tk.Tk()
#window.title('My Window')
#window.geometry('500x300')


#axis_3_frame_plot1 = tkinter.LabelFrame(frame, text="Select X, Y and Z axis")
#axis_3_frame_plot1.grid(row=4, column=0, sticky="news", padx=10, pady=5)

l = tkinter.Label(axis_3_frame_plot, bg='#C060A1', fg='white', width=20, text='0.00')
l.grid(row=3, column=0, sticky="news", padx=10, pady=10)
#l.pack()

def print_selection(v):
    l.config(text='' + v)

s = tk.Scale(axis_3_frame_plot, label='Initial points of range', bg='#C060A1', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s.grid(row=4, column=0)

#window.mainloop()

l1 = tkinter.Label(axis_3_frame_plot, bg='#C060A1', fg='white', width=20, text='0.00')
l1.grid(row=3, column=1, sticky="news", padx=10, pady=10)


def print_selection(v):
    l1.config(text=' ' + v)


s1 = tk.Scale(axis_3_frame_plot, label='Final points of range', bg='#C060A1', fg='white', from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=0,tickinterval=2, resolution=0.01, command=print_selection)
s1.grid(row=4, column=1)

Z2_label_plot1 = tkinter.Label(axis_3_frame_plot, text="Type of X axis scale",)

Z2_combobox_plot1 = ttk.Combobox(axis_3_frame_plot, values=axis_type , state="readonly", width=17)
Z2_combobox_plot1.current(0)
Z2_label_plot1.grid(row=3, column=2)
Z2_combobox_plot1.grid(row=4, column=2)


Z2_label_plot2 = tkinter.Label(axis_3_frame_plot, text="Type of Y axis scale",)

Z2_combobox_plot2 = ttk.Combobox(axis_3_frame_plot, values=axis_type , state="readonly", width=17)
Z2_combobox_plot2.current(0)
Z2_label_plot2.grid(row=3, column=3)
Z2_combobox_plot2.grid(row=4, column=3)




#l.pack()


#window.mainloop()

window.mainloop()