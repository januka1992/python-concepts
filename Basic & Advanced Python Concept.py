{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "20aedd32",
   "metadata": {},
   "source": [
    "#  !!!!  Python Core Concepts !!!!"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efece8ca",
   "metadata": {},
   "source": [
    "## 1. List In Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e5303f7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Print first item :: p\n",
      "Print first item :: e\n",
      "Print first item :: b\n"
     ]
    }
   ],
   "source": [
    "my_list = []\n",
    "\n",
    "# list of integers\n",
    "my_list = [1, 2, 3]\n",
    "\n",
    "# list with mixed data types\n",
    "my_list = [1, \"Hello\", 3.4]\n",
    "\n",
    "# List indexing\n",
    "my_list = ['p', 'r', 'o', 'b', 'e']\n",
    "\n",
    "print(\"Print first item :: {}\".format(my_list[0]))\n",
    "print(\"Print first item :: {}\".format(my_list[-1]))\n",
    "print(\"Print first item :: {}\".format(my_list[-2]))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f9418f49",
   "metadata": {},
   "source": [
    "## 2. Dictionary In Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ff743d24",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Print first item :: 2\n",
      "Print first item :: 4\n",
      "Jack\n",
      "None\n",
      "None\n"
     ]
    },
    {
     "ename": "KeyError",
     "evalue": "'address'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyError\u001b[0m                                  Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_6480/223211316.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     25\u001b[0m \u001b[1;31m# KeyError\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 26\u001b[1;33m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmy_dict\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'address'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     27\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyError\u001b[0m: 'address'"
     ]
    }
   ],
   "source": [
    "# dictionary with integer keys\n",
    "my_dict = {1: 'apple', 2: 'ball'} # O(1)\n",
    "\n",
    "# dictionary with mixed keys # metadata\n",
    "my_dict = {'name': 'John', 'lastname': 'Peeter',1: [2, 4, 3]}\n",
    "\n",
    "print(\"Print first item :: {}\".format(my_dict[1][0]))\n",
    "print(\"Print first item :: {}\".format(my_dict[1][1]))\n",
    "\n",
    "# using dict()\n",
    "my_dict = dict({1:'apple', 2:'ball'})\n",
    "\n",
    "my_dict = {'name': 'Jack'}\n",
    "\n",
    "# Output: Jack\n",
    "print(my_dict['name'])\n",
    "\n",
    "# Output: 26 / None\n",
    "print(my_dict.get('age', None))\n",
    "\n",
    "# Trying to access keys which doesn't exist throws error\n",
    "# Output None\n",
    "print(my_dict.get('address'))\n",
    "\n",
    "# KeyError\n",
    "print(my_dict['address'])\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e6a7b21",
   "metadata": {},
   "source": [
    "## 3. Strings In Python"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "8f59ae14",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "str =  programiz\n",
      "str[0] =  p\n",
      "str[-1] =  z\n",
      "str[1:5] =  rogr\n"
     ]
    }
   ],
   "source": [
    "#Accessing string characters in Python\n",
    "str = 'programiz'\n",
    "print('str = ', str)\n",
    "\n",
    "#first character\n",
    "print('str[0] = ', str[0])\n",
    "\n",
    "#last character\n",
    "print('str[-1] = ', str[-1])\n",
    "\n",
    "# slicing 2nd to 5th character\n",
    "print('str[1:5] = ', str[1:5])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a185c729",
   "metadata": {},
   "source": [
    "## 4. Tuples In Python\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "53a208b5",
   "metadata": {},
   "source": [
    "### Unpacking Using Tuples\n",
    "\n",
    "my_tuple = func()   # (\"Asmita\", 25, \"Norway\")\n",
    "\n",
    "name, age, address = func()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "06822701",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 2, 3)\n",
      "(1, 'Hello', 3.4)\n",
      "(3, 4.6, 'dog')\n"
     ]
    }
   ],
   "source": [
    "# Tuple having integers\n",
    "my_tuple = (1, 2, 3)\n",
    "print(my_tuple)\n",
    "\n",
    "# name, age, address\n",
    "\n",
    "my_typle = (\"Asmita\", 25, \"Norway\")\n",
    "\n",
    "# tuple with mixed datatypes\n",
    "my_tuple = (1, \"Hello\", 3.4)\n",
    "print(my_tuple)\n",
    "\n",
    "my_tuple = 3, 4.6, \"dog\"\n",
    "print(my_tuple)\n",
    "\n",
    "# tuple unpacking is also possible\n",
    "a, b, c = my_tuple"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a1f82c18",
   "metadata": {},
   "source": [
    "## 5. Generators In Python"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "851cd8de",
   "metadata": {},
   "source": [
    "### Generator Syntax\n",
    "\n",
    "range(stop)        ---> takes one argument. # start -1, end stop - 1\n",
    "\n",
    "range(start, stop) ---> takes two arguments.  \n",
    "\n",
    "range(start, stop, step) ---> takes three arguments. # 5   Output - 1, 6, 11\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "80505fa4",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (Temp/ipykernel_6480/340310324.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"C:\\Users\\varun\\AppData\\Local\\Temp/ipykernel_6480/340310324.py\"\u001b[1;36m, line \u001b[1;32m2\u001b[0m\n\u001b[1;33m    range(stop) takes one argument. # start -1, end stop - 1\u001b[0m\n\u001b[1;37m                ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# Syntax\n",
    "\n",
    "# Object --> Next\n",
    "\n",
    "# example\n",
    "for i in range(1, 20):\n",
    "    print(i, end=\" \")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
