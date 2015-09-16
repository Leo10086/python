#_*_ coding:utf-8 _*_
__author__ = 'Administrator'
#以正确的长度在“马路”上打印一段居中的文字
sentence = raw_input("sentence:")

screen_wideth = 70
text_width = len(sentence)
road_width = text_width + 6
left_margin = (screen_wideth - road_width) // 2

print
print'' * left_margin + '+' + '-' * (road_width-4) + '+'
print'' * left_margin + '|' + ' ' * text_width     + '|'
print'' * left_margin + '|' +       sentence       + '|'
print'' * left_margin + '|' + ' ' * text_width     + '|'
print'' * left_margin + '+' + '-' * (road_width-4) + '+'
print