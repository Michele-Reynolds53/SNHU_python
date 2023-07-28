oldest_people = [122, 119, 117, 117, 116]  # Source: Wikipedia.org

nth_person = int(input('Enter N (1-5): '))

if (nth_person >= 4):
    print('The {}th oldest person lived 122 years' \
        .format(nth_person, oldest_people[nth_person-1]))
if (nth_person == 1):
    print('The {}st oldest person lived 122 years' \
        .format(nth_person, oldest_people[nth_person-1]))
if (nth_person == 2):
    print('The {}nd oldest person lived 122 years' \
        .format(nth_person, oldest_people[nth_person-1]))
if (nth_person == 3):
    print('The {}rd oldest person lived 122 years' \
        .format(nth_person, oldest_people[nth_person-1]))