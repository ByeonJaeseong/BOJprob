import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int m = sc.nextInt();
		int n = sc.nextInt();
		String[] board1 = new String[m];
		char[][] board2 = new char[m][n];
		for(int i=0; i<board1.length;i++) {
			board1[i]=sc.next();
		}
		for(int i=0; i<m;i++) {
			for(int j=0; j<n;j++) {
				board2[i][j]=board1[i].charAt(j);
			}
		}
		char[][] board3= new char[8][8];
		char[][] board4 = new char[8][8];
		for(int i=0;i<8;i++) {
			if(i%2==0) {
				board3[0][i]='B';
			}else {
				board3[0][i]='W';
			}
		}
		for(int i=0;i<8;i++) {
			if(i%2==0) {
				board4[0][i]='W';
			}else {
				board4[0][i]='B';
			}
		}
		
		for(int i=0; i<8;i++) {
			if(board3[0][i]=='B') {
				for(int j=1;j<8;j++) {
					if(j%2==0) {
						board3[j][i]='B';
					}else {
						board3[j][i]='W';
					}
				}
			}else {
				for(int j=1;j<8;j++) {
				if(j%2==0) {
					board3[j][i]='W';
				}else {
					board3[j][i]='B';
				}
			}
		}
		}
		
		for(int i=0; i<8;i++) {
			if(board4[0][i]=='B') {
				for(int j=1;j<8;j++) {
					if(j%2==0) {
						board4[j][i]='B';
					}else {
						board4[j][i]='W';
					}
				}
			}else {
				for(int j=1;j<8;j++) {
				if(j%2==0) {
					board4[j][i]='W';
				}else {
					board4[j][i]='B';
				}
			}
		}
		}
		
		
		int c=32;
		for(int l=0; l<=n-8; l++) {
		for(int k=0; k<=m-8;k++) {
			int a=0;
			int b=0;
		for(int i=0; i<8; i++) {
			for(int j = 0; j<8; j++) {
				if(board2[i+k][j+l]!=board3[i][j]) {
					a++;
				}
				if(board2[i+k][j+l]!=board4[i][j]) {
					b++;
				}
			}
		}
		if(a<=b && a<c) {
			c=a;
		}else if(b<a && b<c) {
			c=b;
		}
		}
		}
		System.out.println(c);
		
		

		/*
		for(int i=0; i<8;i++) {
			for(int j=0; j<8;j++) {
				System.out.print(board3[i][j]);
			}
			System.out.println();
		}
		System.out.println();
		for(int i=0; i<8;i++) {
			for(int j=0; j<8;j++) {
				System.out.print(board4[i][j]);
			}
			System.out.println();
		}
		*/
		/*
		System.out.println();
		for(int i=0; i<m;i++) {
			for(int j=0; j<n;j++) {
				System.out.print(board2[i][j]);
			}
			System.out.println();
		}*/


		
		

	}
	
	

}
