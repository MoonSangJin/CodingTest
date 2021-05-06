function solution(answers) {
  let answer = [];
  let one = [1, 2, 3, 4, 5];
  let two = [2, 1, 2, 3, 2, 4, 2, 5];
  let three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  let one_number = 0;
  let two_number = 0;
  let three_number = 0;
  for (let i = 0; i < answers.length; i++) {
    if (answers[i] == one[i % one.length]) {
      one_number += 1;
    }
    if (answers[i] == two[i % two.length]) {
      two_number += 1;
    }
    if (answers[i] == three[i % three.length]) {
      three_number += 1;
    }
  }
  let temp = [];
  temp.push(one_number, two_number, three_number);

  let max_number = Math.max(...temp);

  for (let i = 0; i < temp.length; i++) {
    if (max_number === temp[i]) {
      answer.push(i + 1);
    }
  }

  return answer;
}
