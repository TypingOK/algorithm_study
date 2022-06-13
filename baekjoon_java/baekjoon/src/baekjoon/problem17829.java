package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class problem17829 {
	static int[][] map;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		map = new int[N][N];
		for(int i=0; i<N; i++) {
			String str[] = br.readLine().split(" ");
			for(int j=0; j<N; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		int answer = Divid(N, 0,0);
		System.out.println(answer);
	}
	
	static int Divid(int N, int x, int y) {
		ArrayList<Integer> list = new ArrayList<>();
		if(N==2) {
			list.add(map[x][y]);
			list.add(map[x+1][y]);
			list.add(map[x][y+1]);
			list.add(map[x+1][y+1]);

			Collections.sort(list);
			
			return list.get(2);
		}
		list.clear();
		list.add(Divid(N/2,x,y));
		list.add(Divid(N/2,x+N/2,y));
		list.add(Divid(N/2,x,y+N/2));
		list.add(Divid(N/2,x+N/2,y+N/2));
		
		Collections.sort(list);
		
		return list.get(2);
	}

}
