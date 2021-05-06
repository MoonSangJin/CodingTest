function solution(lottos, win_nums) {
    let answer = [];
    let cnt=0;
    let cnt_zero=0;
    for(let i=0; i<win_nums.length; i++){
        if(win_nums.includes(lottos[i])){
            cnt+=1;
        }else if(lottos[i]===0){
            cnt_zero+=1;
        }
    }
    let best=7-(cnt+cnt_zero);
    let worst=7-(cnt);
    
    if(best>=6){
        answer.push(6);
    }else{
        answer.push(best);
    }
    if(worst>=6){
        answer.push(6);
    }else{
        answer.push(worst);
    }
    

    return answer;
}