package baekjoon;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class problem2477 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cham = sc.nextInt();
		ArrayList<int[]> arr = new ArrayList<>();
		int maxNorth=0;
		int minNorth=99999;
		int maxEast=0;
		int minEast=99999;
		for(int i=0; i<6; i++) {
			int[] temp = new int[2];
			temp[0]=sc.nextInt();
			temp[1]=sc.nextInt();
			if(temp[0]==1&& temp[1]>maxNorth) {
				maxNorth=temp[1];
			}
			if(temp[0]==2 && temp[1]>maxNorth) {
				maxNorth=temp[1];
			}
			if(temp[0]==1 && temp[1]<minNorth) {
				minNorth=temp[1];
			}
			if(temp[0]==2 && temp[1]<minNorth) {
				minNorth=temp[1];
			}
			if(temp[0]==3 && temp[1]>maxEast) {
				maxEast=temp[1];
			}
			if(temp[0]==4 && temp[1]>maxEast) {
				maxEast=temp[1];
			}
			if(temp[0]==3&& temp[1]<minEast) {
				minEast=temp[1];
			}
			if(temp[0]==4 && temp[1]<minEast) {
				minEast=temp[1];
			}
		}
		int a = (maxNorth*maxEast)-(minNorth*minEast);
		System.out.println(a*cham);
	}

}
