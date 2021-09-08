from random import randint as rint
import pprint


def random_scores(school_class):
    scores = [rint(2, 5) for _ in range(rint(3, 7))]
    return {'school_class': school_class, 'scores': scores}


def main():
    classes = [str(k) + m for k in range(1, 12) for m in 'абв']
    school_scores = [random_scores(school_class) for school_class in classes]

    scores_average = []
    scores_sum = 0
    scores_count = 0
    all_class_scores = []
    for class_scores in school_scores:
        scores = class_scores['scores']
        average = round(sum(scores) / len(scores), 2)
        class_scores['average'] = average

        scores_average.append(average)
        scores_sum += sum(scores)
        scores_count += len(scores)
        all_class_scores += scores

    school_average1 = round(sum(scores_average) / len(scores_average), 2)
    school_average2 = round(scores_sum / scores_count, 2)
    school_average3 = round(sum(all_class_scores) / len(all_class_scores), 2)

    pprint.pprint(school_scores)
    print(f'Средний балл по школе 1: {school_average1} (неправильный)')
    print(f'Средний балл по школе 2: {school_average2}')
    print(f'Средний балл по школе 3: {school_average3}')


if __name__ == '__main__':
    main()
