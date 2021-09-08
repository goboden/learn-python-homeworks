from random import randint as rint
import pprint


def random_scores(school_class):
    scores = [rint(2, 5) for _ in range(rint(3, 7))]
    return {'school_class': school_class, 'scores': scores}


def main():
    classes = [str(k) + m for k in range(1, 12) for m in 'абв']
    school_scores = [random_scores(school_class) for school_class in classes]

    scores_average = []
    for class_scores in school_scores:
        scores = class_scores['scores']
        average = round(sum(scores) / len(scores), 2)
        class_scores['average'] = average
        scores_average.append(average)
    school_average = round(sum(scores_average) / len(scores_average), 2)

    pprint.pprint(school_scores)
    print(f'Средний балл по школе: {school_average}')


if __name__ == '__main__':
    main()
