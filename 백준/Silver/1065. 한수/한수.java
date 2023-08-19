import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a;
		a = sc.nextInt();
		int b=0;
		boolean[] isHan = new boolean[a+1];
		for(int i=0; i<=a; i++) {
			isHan[i] = Han(i);
			
		}
		for(int i=0; i<=a; i++) {
			if(isHan[i]==true) {
				b++;
			}
		}
		
		if(a<1000) {
		System.out.println(b-1);
		}else {
			System.out.println(b-2);}
		
		

	}




static boolean Han(int n){
	int Hn=n;
	int H1=Hn%10;
	int H2= (int)(Hn/10)%10;
	int H3= (int)(Hn/100)%10;			
	while(Hn>0) {
		 if(100<=Hn &&H3-H2!=H2-H1) {
			  break;
		 }else{
			 Hn = (int) Hn/10;
		 }
			  
	}
	if (Hn!=0) {
		return false;
	}else {
		return true;
	}
	

}

}
