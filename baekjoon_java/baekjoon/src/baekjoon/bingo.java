package baekjoon;

import java.io.*;
import java.util.*;

public class bingo{

	private static int m;
	private static boolean[][][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int TC = parse(br.readLine());

		TC: for (int tc = 1; tc <= TC; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = parse(st.nextToken());
			m = parse(st.nextToken());

			// user
			Point[][] bingo = new Point[n][m * m + 1];
			board = new boolean[n][m][m];
			int[] bingoCnt = new int[n];

			for (int i = 0; i < n; i++) { // 사용자 수만큼 반복
				for (int j = 0; j < m; j++) {
					st = new StringTokenizer(br.readLine());
					for (int k = 0; k < m; k++) {
						int tmp = parse(st.nextToken());
						bingo[i][tmp] = new Point(j, k);
					}
				}
			} // 사용자별 좌표 저장 완료
			
//			for(int i=0;  i<n; i++) {
//				for(int j=0; j<m*m+1; j++) {
//					System.out.print(bingo[i][j]);
//				}
//				System.out.println();
//			}
			// 사회자 부르기
			st = new StringTokenizer(br.readLine());
			while (st.hasMoreTokens()) { // 최대 m*m
				int now = parse(st.nextToken());

				for (int i = 0; i < n; i++) {
					Point p = bingo[i][now];
					System.out.println(p.x+" "+p.y);
					board[i][p.x][p.y] = true;
					if (colCheck(i, p.x, p.y))
						bingoCnt[i]++;
					if (rowCheck(i, p.x, p.y))
						bingoCnt[i]++;

					if (p.x == p.y && leftDiagonalCheck(i, p.x, p.y)) // ⬉ 방향
						bingoCnt[i]++;
					if (p.x + p.y + 1 == m && rightDiagonalCheck(i, p.x, p.y)) // ⬈ 방향
						bingoCnt[i]++;
					System.out.println(i+" :  "+bingoCnt[i]);
					if (bingoCnt[i] >= m) {
						System.out.println("#" + tc + " " + (i + 1));
						continue TC;
					}
				}
			}
		}
	}

	private static boolean colCheck(int user, int i, int j) {
		for (int jj = 0; jj < m; jj++) {
			if (!board[user][i][jj])
				return false;
		}
		return true;
	}

	private static boolean rowCheck(int user, int i, int j) {
		for (int ii = 0; ii < m; ii++) {
			if (!board[user][ii][j])
				return false;
		}
		return true;
	}

	private static boolean leftDiagonalCheck(int user, int i, int j) { // ⬉ 방향
		for (int ii = 0; ii < m; ii++) {
			if (!board[user][ii][ii])
				return false;
		}
		return true;
	}

	private static boolean rightDiagonalCheck(int user, int i, int j) { // ⬈ 방향
		for (int ii = 0; ii < m; ii++) {
			if (!board[user][ii][m - ii - 1])
				return false;
		}
		return true;
	}

	private static class Point {
		int x, y;

		Point(int x, int y) {
			this.x = x;
			this.y = y;
		}

		@Override
		public String toString() {
			return "Point [x=" + x + ", y=" + y + "]";
		}
		
	}

	private static int parse(String s) {
		return Integer.parseInt(s);
	}
}
