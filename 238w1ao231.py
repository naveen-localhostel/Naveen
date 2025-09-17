{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7a2844e3-6607-49b8-aa96-c6627a961fa7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "enter name naveen\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "my name is naveen.\n"
     ]
    }
   ],
   "source": [
    "#print name by the useer\n",
    "a=input(\"enter name\")\n",
    "print(f\"my name is {a}.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "60989466-4d68-45ae-9ad6-5148da752d1a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nani\n"
     ]
    }
   ],
   "source": [
    "#print name\n",
    "name=\"nani\"\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1924b4cf-d9f4-4c8a-adf3-6f5a1c2b899d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n",
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number1: 2\n",
      "number2: 4\n"
     ]
    }
   ],
   "source": [
    "#print of numbers\n",
    "num1 =int(input())\n",
    "num2=int(input())\n",
    "print(\"number1:\",num1)\n",
    "print(\"number2:\",num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "13beb933-34ed-43c9-bb52-a3edf3597d42",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12\n"
     ]
    }
   ],
   "source": [
    "#addition of two numbers\n",
    "num1=int(input())\n",
    "num2=int(input())\n",
    "print(num1+num2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2ec2176d-9a69-4735-91da-604fbdb33443",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Hello \n",
      " World!\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello  World!\n"
     ]
    }
   ],
   "source": [
    "#concatenate of words\n",
    "word1=input()\n",
    "word2=input()\n",
    "concatenate= word1+ \" \"+word2\n",
    "print(concatenate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9ca6e6e9-c16b-42b6-854e-48951cc43100",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n",
      " 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "3\n",
      "3 7\n"
     ]
    }
   ],
   "source": [
    "#swapping of numbers\n",
    "a=int(input())\n",
    "b=int(input())\n",
    "a=a+b\n",
    "b=a-b\n",
    "a=a-b\n",
    "print(a)\n",
    "print(b)\n",
    "#with 3 variable\n",
    "c=a\n",
    "a=b\n",
    "b=c\n",
    "print(a,b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "e2db1773-1314-4c99-98a1-4023391a8f2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'str'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "#write primitive data type\n",
    "a=10\n",
    "b=\"hello\"\n",
    "c=2.43\n",
    "print(type(a))\n",
    "print(type(b))\n",
    "print(type(c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5eb1f756-4fdf-4237-959f-39b4d020d8d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n",
      "<class 'dict'>\n",
      "<class 'set'>\n"
     ]
    }
   ],
   "source": [
    "#non-primitive types\n",
    "x=[4,5,6]\n",
    "dict_={name:\"nani\"}\n",
    "z={2,4,56,78,9}\n",
    "print(type(x))\n",
    "print(type(dict_))\n",
    "print(type(z))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "aa5afa32-52f9-4234-9497-db015daf3536",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "16\n"
     ]
    }
   ],
   "source": [
    "#square\n",
    "a=int(input())\n",
    "print(a**2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "636e1f5a-f2de-4a85-acc2-188dca24ddac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n",
      " 4\n",
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3.6666666666666665\n"
     ]
    }
   ],
   "source": [
    "#avg of three numbers\n",
    "a=int(input())\n",
    "b=int(input())\n",
    "c=int(input())\n",
    "sum=a+b+c\n",
    "print(sum/3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "38ec019a-4124-4fd0-8501-fc96740ea457",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "40\n"
     ]
    }
   ],
   "source": [
    "#multiple\n",
    "num1=int(input())\n",
    "print(num1*10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "574ae0b6-0172-4072-ae75-ed54237a6284",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.08333333333333333\n"
     ]
    }
   ],
   "source": [
    "#mintues into seconds\n",
    "a=int(input())\n",
    "print(a/60)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "30868df8-68ed-4f5e-b6f2-78641542ff26",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3.56\n",
      " 4.78\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "17.0168\n"
     ]
    }
   ],
   "source": [
    "#mutliply of float \n",
    "a=float(input())\n",
    "b=float(input())\n",
    "print(a*b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d1e4b8c8-fae8-4055-8409-6691837ce68d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3\n",
      " 5\n",
      " 4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n"
     ]
    }
   ],
   "source": [
    "#large numbers\n",
    "a=int(input())\n",
    "b=int(input())\n",
    "c=int(input())\n",
    "print(max(a,b,c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "5407c229-b2a4-4441-a1e3-97503a78fdef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "print(a*(a+1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "67198577-8421-4c7b-b395-77f9727a72c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "for i in range(2,a+1):\n",
    "    if i%2==0:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "d9c33a1d-79de-4ebd-a897-512589233d48",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " True\n",
      " True\n",
      " 800\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "loan approved\n"
     ]
    }
   ],
   "source": [
    "pan=bool(input())\n",
    "adhar=bool(input())\n",
    "cibil=int(input())\n",
    "if (pan and adhar and cibil>750):\n",
    "    print(\"loan approved\")\n",
    "else:\n",
    "    print(\"rejected\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "521fa24a-048a-4e84-b745-e5da7cd8a15a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 4\n",
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "-2\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "print(a+b)\n",
    "print(a-b)\n",
    "print(a//b)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "559e2747-d161-4392-8b7a-78b0a85530ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 5\n",
      " 7\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n",
      "False\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "b=int(input())\n",
    "print( a>10 and b<5)\n",
    "print(a==10 or b>10)\n",
    "print( not(a==10))\n",
    "      "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "3c122044-f3b4-49e3-9a85-fe95272a4dd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "positive\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "if a>0:\n",
    "    print(\"positive\")\n",
    "elif a<0:\n",
    "    print(\"negative\")\n",
    "else:\n",
    "    print(\"Zero\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e0ceb512-8371-401d-aa7f-0a6a958e83c4",
   "metadata": {},
   "outputs": [
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[38], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m a\u001b[38;5;241m=\u001b[39m\u001b[38;5;28mint\u001b[39m(\u001b[38;5;28minput\u001b[39m())\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m a\u001b[38;5;241m%\u001b[39m\u001b[38;5;241m2\u001b[39m\u001b[38;5;241m==\u001b[39m\u001b[38;5;241m0\u001b[39m:\n\u001b[0;32m      3\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124meven\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1262\u001b[0m, in \u001b[0;36mKernel.raw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m   1260\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mraw_input was called, but this frontend does not support input requests.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1261\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m StdinNotImplementedError(msg)\n\u001b[1;32m-> 1262\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_input_request(\n\u001b[0;32m   1263\u001b[0m     \u001b[38;5;28mstr\u001b[39m(prompt),\n\u001b[0;32m   1264\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_parent_ident[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m],\n\u001b[0;32m   1265\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mget_parent(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mshell\u001b[39m\u001b[38;5;124m\"\u001b[39m),\n\u001b[0;32m   1266\u001b[0m     password\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mFalse\u001b[39;00m,\n\u001b[0;32m   1267\u001b[0m )\n",
      "File \u001b[1;32mC:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel\\kernelbase.py:1305\u001b[0m, in \u001b[0;36mKernel._input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m   1302\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[0;32m   1303\u001b[0m     \u001b[38;5;66;03m# re-raise KeyboardInterrupt, to truncate traceback\u001b[39;00m\n\u001b[0;32m   1304\u001b[0m     msg \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInterrupted by user\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m-> 1305\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m(msg) \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1306\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mException\u001b[39;00m:\n\u001b[0;32m   1307\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mlog\u001b[38;5;241m.\u001b[39mwarning(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mInvalid Message:\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39m\u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "if a%2==0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "21a80d99-cefd-49c2-b723-6c5d56d0f40c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 55\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "divisible\n"
     ]
    }
   ],
   "source": [
    "a=int(input())\n",
    "if a%5==0 or a%11==0:\n",
    "    print(\"divisible\")\n",
    "else:\n",
    "    print(\"not divisible\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "d9701485-5832-4aef-be5f-ea80462e27e0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 50\n",
      " 34\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pass 84\n"
     ]
    }
   ],
   "source": [
    "theory=int(input())\n",
    "pratical=int(input())\n",
    "total=theory+pratical\n",
    "if (theory>35 and pratical>30 and total):\n",
    "    print(\"pass\",total)\n",
    "else:\n",
    "    print(\"fail\",total)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "0c0913a0-3a32-4706-9482-deea078b7c9a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 45\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "adult\n"
     ]
    }
   ],
   "source": [
    "#day2\n",
    "age=int(input())\n",
    "if age<=12:\n",
    "    print(\"child\")\n",
    "elif 12<age<20:\n",
    "    print(\" teenage\")\n",
    "else:\n",
    "    print(\"adult\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "0540d359-36f5-4bb6-8eda-4cc18a65a717",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 90\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A\n"
     ]
    }
   ],
   "source": [
    "marks=int(input())\n",
    "if marks>=90:\n",
    "    print(\"A\")\n",
    "elif 70<marks<90:\n",
    "    print(\"b\")\n",
    "elif 50<marks<70:\n",
    "    print(\"c\")\n",
    "elif 40<marks<50:\n",
    "    print(\"d\")\n",
    "else:\n",
    "    print(\"fail\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60b7247b-d07d-4e33-b952-32e6940599dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "user=\"nani\"\n",
    "password=1234\n",
    "username=input()\n",
    "if username==user:\n",
    "    print(\"correcr usernanme\")\n",
    "    psd=int(input())\n",
    "    if psd==password:\n",
    "        print(\"correct password\")\n",
    "        print(\"login successfully\")\n",
    "    else:\n",
    "        print(\" invalid password\")\n",
    "        \n",
    "        psd=int(input())\n",
    "        if psd==password:\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "         \n",
    "            \n",
    "            print(\"correct password\")\n",
    "            print(\"login successfully\")\n",
    "        \n",
    "else:\n",
    "    print(\" invaild username\")\n",
    "        \n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9363ab79-77fa-4187-96f5-bc1d1988a3d4",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
