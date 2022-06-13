package swea;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class problem2383 {
	
	static Queue<Person>[] ps; // 현재 들어가 있는 계단의 큐
	static ArrayList<Person> persons; // 사람들 저장할 리스트
	static boolean[] visit; // 계단으로 들어갔는지 체크
	static int N,answer;
	static Stair[] stairs; // 계단을 담을 배열
	
	
	static class Person {
		int x,y;
		int moveTime;
		int stairTime;
		int number;
		Person(int x,int y){
			this.x=x;
			this.y=y;
		}

	}
	
	static class Stair{
		int x,y;
		int k;
		Stair(int x,int y,int k){
			this.x=x;
			this.y=y;
			this.k=k;
		}
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int TC = sc.nextInt();
		for(int tc=1; tc<=TC; tc++) {
			N = sc.nextInt();
			persons = new ArrayList<>();
			stairs = new Stair[2];
			answer = Integer.MAX_VALUE;
			ps= new LinkedList[2];
			ps[0] = new LinkedList<>();
			ps[1] = new LinkedList<>();
			
			
			int index=0;
			for(int i=1; i<=N; i++) {
				for(int j=1; j<=N; j++) {
					int a = sc.nextInt();
					if(a==0) {
						continue;
					}
					else if(a==1) {
						persons.add(new Person(i,j));
					}else {
						stairs[index] = new Stair(i,j,a);
						index++;
					}
				}
			}
			
			
			comb(0);
			
			System.out.println("#"+tc+" "+answer);
		}
	}
	
	
	public static void comb(int index) {
		if(index == persons.size()) {
			int count = simulation();
			
			answer= Math.min(count, answer);
			return;
		}
		
		persons.get(index).number = 0; // 1번째 계단 이용하기
		persons.get(index).moveTime = Math.abs(persons.get(index).x-stairs[0].x)+Math.abs(persons.get(index).y-stairs[0].y);
		comb(index+1);
		persons.get(index).number = 1; // 2번째 계단 이용하기
		persons.get(index).moveTime = Math.abs(persons.get(index).x-stairs[1].x)+Math.abs(persons.get(index).y-stairs[1].y);
		comb(index+1);
	}

	public static int simulation() {
		
		visit = new boolean[persons.size()];
		
		int time=1; // 1 분부터 진행
		int cnt=0; //사람 카운트
		
		while(true) {
			for(int i =0; i<2; i++) {
				int size = ps[i].size();
				
				for(int j=0; j<size; j++) {
					Person p = ps[i].poll();
					Stair s = stairs[p.number];
					
					if(p.stairTime+s.k <= time) { // 계단 내려가는 시간을 더한 값이 현재 지난 분보다 작거나 같다면
						continue; // 탈출 성공
					}
					
					ps[i].offer(p); //아니면 다시 큐에 집어넣기
				}
			}
			
			if(cnt == persons.size() && ps[0].isEmpty() && ps[1].isEmpty()) { // 전부 내려갔다면 시간을 반환
				return time;
			}
			
			for(int i=0; i<persons.size(); i++) {
				if(visit[i]) { // 이미 계단을 내려가고 있는 중이라면
					continue;
				}
				if(persons.get(i).moveTime+1 <= time && ps[persons.get(i).number].size()<3) { //계단 밖에서 대기 
					visit[i] = true;
					persons.get(i).stairTime = time; //바로 들어간게 아니기 때문에 기다린 만큼 계단에 입장한 시간을 넣어준다.
					ps[persons.get(i).number].offer(persons.get(i));
					cnt++;
				}
			}
			
			time++;
		}
	}
}
