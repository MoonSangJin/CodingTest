function solution(array, commands) {
  let answer = [];
  for (let i = 0; i < commands.length; i++) {
    let temp = array
      .slice(commands[i][0] - 1, commands[i][1])
      .sort((a, b) => a - b); //js의 기본 sort는 문자열으로 변환시키고 sort함으로 숫자비교시 (a,b)=>return a-b
    answer.push(temp[commands[i][2] - 1]);
  }
  return answer;
}
