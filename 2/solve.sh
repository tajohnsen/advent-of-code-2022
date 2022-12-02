#!/usr/bin/env bash


: '
A = X = ROCK
B = Y = PAPER
C = Z = SCISSORS
'


function points1()
{
  ROCK=1
  PAPER=2
  SCISSORS=3

  WIN=6
  TIE=3
  LOSE=0

  if [[ $1 == A ]]; then
    if [[ $2 == X ]]; then
      echo $((ROCK + TIE))
    elif [[ $2 == Y ]]; then
      echo $((PAPER + WIN))
    elif [[ $2 == Z ]]; then
      echo $((SCISSORS + LOSE))
    fi
  elif [[ $1 == B ]]; then
    if [[ $2 == X ]]; then
      echo $((ROCK + LOSE))
    elif [[ $2 == Y ]]; then
      echo $((PAPER + TIE))
    elif [[ $2 == Z ]]; then
      echo $((SCISSORS + WIN))
    fi
  elif [[ $1 == C ]]; then
   if [[ $2 == X ]]; then
      echo $((ROCK + WIN))
    elif [[ $2 == Y ]]; then
      echo $((PAPER + LOSE))
    elif [[ $2 == Z ]]; then
      echo $((SCISSORS + TIE))
    fi
  fi
}


: '
X = LOSE
Y = TIE
Z = WIN
'


function points2()
{
  ROCK=1
  PAPER=2
  SCISSORS=3

  WIN=6
  TIE=3
  LOSE=0

  if [[ $1 == A ]]; then
    if [[ $2 == X ]]; then
      echo $((SCISSORS + LOSE))
    elif [[ $2 == Y ]]; then
      echo $((ROCK + TIE))
    elif [[ $2 == Z ]]; then
      echo $((PAPER + WIN))
    fi
  elif [[ $1 == B ]]; then
    if [[ $2 == X ]]; then
      echo $((ROCK + LOSE))
    elif [[ $2 == Y ]]; then
      echo $((PAPER + TIE))
    elif [[ $2 == Z ]]; then
      echo $((SCISSORS + WIN))
    fi
  elif [[ $1 == C ]]; then
   if [[ $2 == X ]]; then
      echo $((PAPER + LOSE))
    elif [[ $2 == Y ]]; then
      echo $((SCISSORS + TIE))
    elif [[ $2 == Z ]]; then
      echo $((ROCK + WIN))
    fi
  fi
}


TOTAL1=0
TOTAL2=0
while read -r line; do
  them=$(cut -d\  -f1 <(echo ${line}))
  me=$(cut -d\  -f2 <(echo ${line}))
  score1=$(points1 ${them} ${me})
  score2=$(points2 ${them} ${me})
  TOTAL1=$((TOTAL1 + score1))
  TOTAL2=$((TOTAL2 + score2))
done < input
 
echo Total points for round 1: $TOTAL1
echo Total points for round 2: $TOTAL2
