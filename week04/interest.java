public class interest {
public static void main(String[] args) {
int years = 10;
double principal_amount = 1_000.00;
double interest = 0.05;
for (int y = 0; y < years; y++) {
double  amount_at_end_of_year = principal_amount * (1.0 + interest);
principal_amount = amount_at_end_of_year;
}
System.out.println(principal_amount);
}
}
