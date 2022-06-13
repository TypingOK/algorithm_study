package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class problem16954 {

	static int dx[] = { 0, -1, -1, 0, 1, 1, 1, 0, -1 };
	static int dy[] = { 0, 0, 1, 1, 1, 0, -1, -1, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int map[][] = new int[8][8];

		for (int i = 0; i < 8; i++) {
			char c[] = br.readLine().toCharArray();
			for (int j = 0; j < 8; j++) {
				if (c[j] == '.') {
					map[i][j] = 0;
				} else if (c[j] == '#') {
					map[i][j] = 1;
				}
			}
		}
		int copy[][] = new int[8][8];
		copy[7][0] = 2;
		if (BFS(map, copy)) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}

	}

	static boolean BFS(int[][] map, int[][] copy) {
		Queue<int[]> q = new LinkedList<int[]>();

		q.add(new int[] { 7, 0 });

		int size = 1;
		while (!q.isEmpty()) {
			size = q.size();
			for (int i = 0; i < size; i++) {
				int[] temp = q.poll();
				if (temp[0] == 0 && temp[1] == 7) {
					return true;
				}
				if (map[temp[0]][temp[1]] == 1) {
					copy[temp[0]][temp[1]] = 0;
					continue;
				}else {
					for (int j = 0; j < 9; j++) {
						int nx = temp[0] + dx[j];
						int ny = temp[1] + dy[j];
						if (0 <= nx && nx < 8 && 0 <= ny && ny < 8 && map[nx][ny] != 1) {
							copy[temp[0]][temp[1]] = 0;
							copy[nx][ny] = 2;
							q.add(new int[] { nx, ny });
						}
					}
				}
			}
			down(map);
//			print(map);
//			print(copy);
//			System.out.println("======================================");
			if (!check(copy)) {
				return false;
			}
			if(check2(map)) {
				return true;
			}
			
		}

		return false;
	}
	static boolean check2(int[][] map) {
		for(int i=0; i<8; i++) {
			for(int j=0; j<8; j++) {
				if(map[i][j]==1) {
					return false;
				}
			}
		}
		
		return true;
	}
	static boolean check(int[][] copy) {
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				if (copy[i][j] == 2) {
					return true;
				}
			}
		}
		return false;
	}

	static int[][] down(int[][] map) {
		for (int i = 6; i >= 0; i--) {
			for (int j = 0; j < 8; j++) {
				map[i + 1][j] = map[i][j];

			}
		}
		for (int i = 0; i < 8; i++) {
			map[0][i] = 0;
		}

		return map;
	}

	static void print(int[][] map) {
		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				System.out.print(map[i][j] + " ");
			}
			System.out.println();
		}
		System.out.println();
	}
}
