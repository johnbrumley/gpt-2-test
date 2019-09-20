# so far this kind of works....
#
# but the dataset is mostly trivia stuff, so ot 
# often defaults to that style
# trying to find a database of open-ended questions
# maybe one of zen koans

# maybe there is a section of answers.com that has 
# more of this style. Like "how do I fall in love" ... etc.

import gpt_2_simple as gpt2
import argparse
import re

parser = argparse.ArgumentParser(description='specify the checkpoint')
parser.add_argument('-c', help='specify checkpoint')

args = parser.parse_args()
chckpnt = args.c

def gen_q(a=''):

    # wrapping with start and end strings

    #add a ? to the end to match the format
    if a[-1] is not '?':
        a = a + '?'

    prefix = startString + a + endString

    # see if changing the temperature will affect the questions
    # also try out the top_k and top_p values in case
    # also maybe generate more samples and randomly select from them

    good_q = False

    while not good_q:
        qs = gpt2.generate(sess,
                    run_name=chckpnt,
                    length=100,
                    temperature=0.7,
                    nsamples=1,
                    prefix=prefix,
                    include_prefix=False,
                    truncate=endString,
                    return_as_list=True
                    )

        # for q in qs:
        #     print(q)
        # remove the startString from the question

        q = qs[0]

        # seems like i'm still getting tabs, also multiple spaces in a row
        q = q.replace('\t','')
        q = re.sub(' +',' ', q)

        # print('PRE SPLIT:', q)
        q = q.split(startString)

        if len(q) >= 1:
            q = q[-1]
            good_q = True

    return q

# make sure my checkpoint is in the checkpoint directory

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name=chckpnt)

startString = '<|startoftext|>'
endString = '<|endoftext|>'

# gpt2.generate(sess,
#                 run_name='squad-quest',
#                 length=250,
#                 temperature=0.7,
#                 nsamples=1
#                 )

# generate initial question
qs = gpt2.generate(sess,
                run_name=chckpnt,
                length=100,
                temperature=0.7,
                nsamples=2,
                prefix=startString,
                include_prefix=False,
                truncate=endString,
                return_as_list=True
                )

# slice based on prefix and ending

# for q in qs:
#     print(q)

print('question: ', qs[0])

while True:
    a = input("answer: ")

    q = gen_q(a)

    print('question: ', q)



# gpt2.generate(sess,
#               length=100,
#               temperature=0.7,
#               prefix="the weather today is shit",
#               nsamples=2,
#               batch_size=2,
#               # truncate='<|endoftext|>',
#               include_prefix=False
#               )


# question:  Then I suppose, Socrates, that there is an art in philosophy which conceives and enjoins the thought of men, and which is concerned not with notions of absolute justice but with notions of the just man?
# answer: I can't follow you. Let's talk about poodles
# question:  But tell me, where is the confusion?
# answer: I'm not a philosopher, I am a poodle, a dog, I can only speak in barks
# question:  I can pick up the gavel and I can utter the wail of the ostrich, the chirpy rattle of the ostrich, the whistling of the ostrich, the snorting of the grub and the hoofs of the ostrich -                     Have you noticed how easily friends turn their back on you and your friends?
# answer: An ostrich hides its head in the sand, even amongst friends
# question:  An ostrich hides its head in the sand, even amongst friends<|endoftext|>When do you get one coming?<|startoftext|>He is a good-natured fellow, but what's the hurry?<|startoftext|>When do you get two coming?<|startoftext|>Why?<|startoftext|>You can see the ostrich above; but where do you suppose it to lay its head?<|startoftext|>Do you see the shadow of the ostrich?<|startoftext|>If you don't raise your eyes, how can you see the shadow of the ostrich?<|startoftext|>If you don't raise your eyes, how can you distinguish the shadow of the ostrich?<|startoftext|>CASE  A monk asked Chih Tsang, "The grass on the ground is the ground (the ground) and the ostrich is not?<|startoftext|>63 When you see the shadow of the ostrich, what do you say, Teacher?<|startoftext|>64   What do you say to be born again?<|startoftext|>If you don't raise your eyes, how will you distinguish the shadow
# answer: uh oh