package baekjoon;

import java.util.Scanner;

public class solution17143 {
	static int[] di = {0,-1,+1,0,0}; //1:up, 2:down, 3:right, 4:left;
	static int[] dj = {0,0,0,+1,-1};
	
	
	static Shark[][] mapStart;
	static Shark[][] mapEnd;
	static int ans;
	
	static int fisher;
	static int R,C,M;
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		R = sc.nextInt();
		C = sc.nextInt();
		M = sc.nextInt();
		
		mapStart = new Shark[R+1][C+1];
		mapEnd = new Shark[R+1][C+1];
		
		for(int m=0; m<M; m++) {
			int i = sc.nextInt();
			int j = sc.nextInt();
			int s = sc.nextInt();
			int d = sc.nextInt();
			int w = sc.nextInt();
			
			mapStart[i][j] = new Shark(s,d,w);
		}
		fisher = 0; //맵 왼쪽 0번열에서 출발
		
		while(true) {
			fisher++;
			if(fisher>C) break;
			fishing();
//			print();
			move();
		}
		
		System.out.println(ans);
	}
	
	private static void move() {
		for(int i=1; i<=R; i++) {
			for(int j=1; j<=C; j++) {
				if(mapStart[i][j] !=null) { // 출발해야하는 상어
					Shark now = mapStart[i][j]; // 현재 출발하는 상어 객체
					
					int ni = i+(di[now.dir]*now.speed); //지금 쳐다보는 방향으로 일단 직진
					int nj = j+(dj[now.dir] * now.speed);
					
					while(ni<1 || ni>R) {
						now.dir = reverse(now.dir);
						
						if(ni<1) { // 1보다 위쪽으로 나간 경우
							ni = 1+(1-ni); // 1에서 아래로으로 보내야 하니 뛰쳐 나간 만큼 더해주기
						}else {
							ni = R - (ni - R); // R보다 크면 아래로 나간 경우. R에서 뺄셈으로 돌아오도록 한다.
						}
					}
					while(nj<1 || nj>C) {
						now.dir = reverse(now.dir);
						
						if(nj<1) { // 1보다 왼쪽으로 나간 경우
							nj = 1+(1-nj); // 1에서 오른쪽으로 보내야 하니 뛰쳐 나간 만큼 더해주기
						}else {
							nj = C - (nj - C); // C보다 크면 오른쪽으로 나간 경우. R에서 뺄셈으로 돌아오도록 한다.
						}
					}
					
					if(mapEnd[ni][nj] == null || mapEnd[ni][nj].weight < now.weight) { // 목적지 착륙 조건
						mapEnd[ni][nj] = now;
					}
					
					mapStart[i][j] = null;
				}
			}
		}
		
		for(int i=1; i<=R; i++) {
			for(int j=1; j<=C; j++) {
				mapStart[i][j] = mapEnd[i][j];
				mapEnd[i][j] = null;
			}
		}
	}
	
	static int reverse(int dir) {
		switch(dir) {
		case 1: return 2;
		case 2: return 1;
		case 3: return 4;
		case 4 : return 3;
		}
		return 0;
	}
	
	private static void fishing() {
		for(int i=1; i<=R; i++) {
			if(mapStart[i][fisher] != null) {
				ans+= mapStart[i][fisher].weight;
				mapStart[i][fisher] = null;
				break;
				
			}
		}
	}

	private static void print() {
		for(int i=1; i<=R; i++) {
			for(int j=1; j<=C; j++) {
				System.out.print(mapStart[i][j]!=null? mapStart[i][j].weight : 0);
			}
			System.out.println();
		}
		System.out.println("------------------------------------------");
		
	}
	
	static class Shark{
		int speed,weight,dir;
		
		Shark(int s, int d, int w){
			speed = s;
			dir = d;
			weight = w;
			
		}
	}

}
