function solution(n, computers) {
  var answer = 0;
  let graph = [];
  let visited = [];
  let len = computers.length;
  for (let i = 0; i <= len; i++) {
    graph[i] = [];
    visited[i] = false;
  }
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      if (i != j && computers[i][j] === 1) {
        graph[i + 1].push(j + 1);
      }
    }
  }
  //연결 그래프 만들기

  function dfs(graph, v, visited) {
    visited[v] = true;
    for (let i of graph[v]) {
      if (!visited[i]) {
        dfs(graph, i, visited);
      }
    }
  }
  //dfs돌리기

  for (let i = 1; i <= len; i++) {
    if (visited[i] === false) {
      dfs(graph, i, visited);
      answer += 1;
    }
  }
  return answer;
}
