from Tkinter import*
import tkFileDialog
from recommendations import *
from imdb import IMDb
root = Tk()
root.title("Movie Recommendation Engine")
global selected_item
class GUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.grid(columnspan=1)
        self.widget()
    def widget(self):
        self.var1 = IntVar()
        self.var3 = IntVar()
        self.var1.set(2)
        self.var3.set(2)
        self.frame0 = LabelFrame(root,text="")
        self.label=Label(self.frame0,text="Engine").grid(row=0,column=0)
        self.frame1 = LabelFrame(self.frame0,text="")
        self.movie_based_button = Radiobutton(self.frame1,text='Movie Based',variable=self.var1,value=1).grid(row=0,column=0,padx=2,pady=2)
        self.user_based_button = Radiobutton(self.frame1,text='User Based',variable=self.var1,value=2).grid(row=1,column=0,padx=2,pady=2)
        self.frame1.grid(row=1,column=0)
        self.frame2 = LabelFrame(self.frame0,text="")
        self.similarirty_metric_label = Label(self.frame2,text="Similarity Metric").grid(row=0,column=0,padx=2,pady=2)
        self.pearson_button = Radiobutton(self.frame2,text='Pearson',variable=self.var3,value=1).grid(row=1,column=0,padx=2,pady=2)
        self.euclidean_button = Radiobutton(self.frame2,text='Euclidean',variable=self.var3,value=2).grid(row=2,column=0,padx=2,pady=2)
        self.frame2.grid(row=3,column=0)
        self.upload_ratings_button = Button(self.frame0,text="Upload Ratings",width=12,command=self.upload_ratings).grid(sticky=N,row=4,column=0,padx=2,pady=2)
        self.upload_movies_button = Button(self.frame0,text="Upload Movies",width=12,command=self.upload_movies).grid(sticky=N,row=5,column=0,padx=2,pady=2)
        self.upload_links_button = Button(self.frame0,text="Upload Links",width = 12,command=self.upload_links).grid(sticky=N,row=6,column=0,padx=2,pady=2)
        self.show_button = Button(self.frame0,text="Run",width = 12,bg="red",command=self.run).grid(row=7,column=0,padx=5,pady=5) #I KNOW THIS BUTTON IT IS NOT NEED BUT I PUT ON IT. WHEN YOU SELECT ALL THE THINGS IT IS GOING TO WORK IT
        self.frame0.grid(row=0,column=0,padx=5,pady=5)
        self.frame3 = LabelFrame(root,text="")
        self.movies_users_label = Label(self.frame3,text="Movies/Users").grid(row=0,column=0)
        self.scrollbar = Scrollbar(self.frame3).grid(row=1,column=1,sticky=NS)
        self.movies_users_listbox = Listbox(self.frame3,height=17,selectmode=BROWSE)
        self.movies_users_listbox.bind("<<ListboxSelect>>", self.select_time)
        self.movies_users_listbox.grid(row=1,column=0)
        self.scrollbar = Scrollbar(self.frame3,command=self.movies_users_listbox.yview).grid(row=1,column=1,sticky=NS)
        self.frame3.grid(sticky=N,row=0,column=1,padx=5,pady=5)
        self.frame4 = LabelFrame(root,text="")
        self.movies_users_label = Label(self.frame4,text="Recommended Movie").grid()
        self.movies_users_listbox2 = Listbox(self.frame4,height=17,selectmode=BROWSE)
        self.movies_users_listbox2.bind("<<ListboxSelect>>",self.selected_item2)
        self.movies_users_listbox2.grid()
        self.frame4.grid(sticky=N,row=0,column=2,padx=5,pady=5)
        self.frame5 = LabelFrame(root,text="")
        self.movies_users_label = Label(self.frame5,text="Information").grid()
        self.movies_users_labelframe4 = LabelFrame(self.frame5,text="").grid(sticky=E)
        self.movie_users_labela1 = Label(self.frame5,text="Director:").grid(row=1,column=0)
        self.movie_users_labela2 = Label(self.frame5,text="Stars:").grid(row=2,column=0)
        self.movie_users_labela3 = Label(self.frame5,text="Rating:").grid(row=3,column=0) #"""""""""""""""""""""""""""HERE IS THE LAST PART
        self.movie_users_labela4 = Label(self.frame5,text="Genres:").grid(row=4,column=0)
        self.movie_users_labela4 = Label(self.frame5,text="Plot:").grid(row=5,column=0)
        self.frame5.grid(sticky=N,row=0,column=3,padx=5,pady=5)
    def upload_ratings(self):
        self.file_path0 = tkFileDialog.askopenfilename(title='Upload Ratings')
    def upload_movies(self):
        self.file_path1 = tkFileDialog.askopenfilename(title='Upload Movies')
    def upload_links(self):
        self.file_path2 = tkFileDialog.askopenfilename(title='Upload Links')
    def run(self):
        if self.var1.get() == 1:
            self.var1.set(0)
            pass
        if self.var1.get() == 2:
            for i in range(1,611):
                self.movies_users_listbox.insert(END,i)
            pass
    def select_time(self, val):
        self.sender = val.widget
        self.idx = self.sender.curselection()
        self.value = self.sender.get(self.idx)
        with open(self.file_path0, 'r') as data_file:
            new_data_dict = {}
            data_file.next()
            for row in data_file:
                row = row.strip().split(",")
                username = int(row[0])
                movie_id = int(row[1])
                rating = float(row[2])
                if username in new_data_dict:
                    new_data_dict[username][movie_id] = rating
                else:
                    new_data_dict[username] = {}
                    new_data_dict[username][movie_id] = rating
        with open(self.file_path1, 'r') as data_file:
            new_data_dict1 = {}
            data_file.next()
            for row1 in data_file:
                row1 = row1.strip().split(",")
                username1 = int(row1[0])
                movie_id1 = row1[1]
                if username1 in new_data_dict1:
                    new_data_dict1[username1]=movie_id1
                else:
                    new_data_dict1[username1] = {}
                    new_data_dict1[username1]=movie_id1
        if self.var3.get()==1:
            select_radio_button=sim_pearson
        else:
            select_radio_button=sim_distance
        list_of_recommend = getRecommendations(new_data_dict,self.value,similarity=select_radio_button)
        print list_of_recommend
        for a in list_of_recommend[0:1]:
            top_five_movies1=a[1]
            aa = new_data_dict1[top_five_movies1]
            self.movies_users_listbox2.insert(1,aa)
        for a in list_of_recommend[1:2]:
            top_five_movies2=a[1]
            ab = new_data_dict1[top_five_movies2]
            self.movies_users_listbox2.insert(2,ab)
        for a in list_of_recommend[2:3]:
              top_five_movies3=a[1]
              ac = new_data_dict1[top_five_movies3]
              self.movies_users_listbox2.insert(3,ac)
        for a in list_of_recommend[3:4]:
              top_five_movies4=a[1]
              ad = new_data_dict1[top_five_movies4]
              self.movies_users_listbox2.insert(4,ad)
        for a in list_of_recommend[4:5]:
              top_five_movies5=a[1]
              ae = new_data_dict1[top_five_movies5]
              self.movies_users_listbox2.insert(5,ae)
        return new_data_dict
    def selected_item2(self, val1):
        self.sender1 = val1.widget
        self.idx1 = self.sender1.curselection()
        self.value1 = self.sender1.get(self.idx1)   #"""""""""""""""""""""""""WHEN USER CLICK THE LISTBOX-2 IT IS GOING TO DELETE ALL THE DATA AND HE CAN SELECT OTHER USERS AND SEE OTHER RECOMMENDED USERS
        with open(self.file_path2, 'r') as data_file:
            new_data_dict2 = {}
            data_file.next()
            for row in data_file:
                row = row.strip().split(",")
                username2 = int(row[0])
                movie_id2 = row[1]
                if username2 in new_data_dict2:
                    new_data_dict2[username2] = movie_id2
                else:
                    new_data_dict2[username2] = {}
                    new_data_dict2[username2] = movie_id2
        with open(self.file_path1, 'r') as data_file:
            new_data_dict1 = {}
            data_file.next()
            for row1 in data_file:
                row1 = row1.strip().split(",")
                username1 = int(row1[0])
                movie_id1 = row1[1]
                if username1 in new_data_dict1:
                    new_data_dict1[movie_id1]=username1
                else:
                    new_data_dict1[movie_id1] = {}
                    new_data_dict1[movie_id1]=username1
        real_number = new_data_dict1[self.value1]
        ia = IMDb()
        the_matrix = ia.get_movie(real_number)
        b = (the_matrix['director'])
        self.label2 = Label(self.frame5,text=b).grid(row=1,columm=1)
        ia1 = IMDb()
        the_matrix = ia1.get_movie(real_number)
        c = (the_matrix['plot'])
        self.label3 = Label(self.frame5,text=c).grid(row=5,columm=1)
        ia2 = IMDb()
        the_matrix = ia2.get_movie(real_number)
        d = the_matrix.get("cast")
        self.label4 = Label(self.frame5,text=d).grid(row=2,columm=1)
        ia3 = IMDb()
        the_matrix = ia3.get_movie(real_number)
        e = the_matrix.get("rating")
        self.label5 = Label(self.frame5,text=e).grid(row=3, columm=1)
        self.movies_users_listbox2.delete(0, END)
app = GUI(root)
root.mainloop()
