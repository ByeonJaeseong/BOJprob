import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.PatternSyntaxException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String cal = bf.readLine();
		String[] mArray = cal.trim().split("-");
		int a =0;
		for(int i=0; i<mArray.length; i++) {
			int p =0;
			try {
			//System.out.println("실행되었습니다.");
			String[] pArray = mArray[i].trim().split("\\+");
			//split 에러 피하려면 + [ ] , ( ) 같은 문자에는 \\ 사용할것!
			for(int j=0; j<pArray.length; j++) {
				p+=Integer.parseInt(pArray[j]);
			}
			if(i==0) {
				a+=p;
			}else {
				a-=p;
			}
			//System.out.println("에러 발생하지 않았습니다.");
			}catch(PatternSyntaxException e) {
				//e.printStackTrace();
			//System.out.println(mArray[i]);
				if(i==0) {
					a+=Integer.parseInt(mArray[i]);
				}else {
					a-=Integer.parseInt(mArray[i]);
				}
			//System.out.println("에러 발생");
			}
		}
		System.out.print(a);

	}

}
