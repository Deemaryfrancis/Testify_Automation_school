package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task9 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();
        //Maximize the browser
        driver.manage().window().maximize();
        //Navigate to the url
        driver.get("https://www.saucedemo.com/");
        //Get username
        String userName = driver.findElement(By.xpath("//div[@id='login_credentials']")).getText();
        //Password
        String password = driver.findElement(By.cssSelector(".login_password")).getText();

        userName = userName.substring(24,38);
        password = password.substring(23,36);

//        System.out.println(userName);
//        System.out.println("--------");
//        System.out.println(password);

        //Login
        driver.findElement(By.id("user-name")).sendKeys(userName);
        Thread.sleep(2000);
        driver.findElement(By.id("password")).sendKeys(password);
        Thread.sleep(2000);
        driver.findElement(By.id("login-button")).click();
        Thread.sleep(3000);

        driver.navigate().back();
        Thread.sleep(3000);
        String loginValue = driver.findElement(By.id("login-button")).getAttribute("value");
        System.out.println(loginValue);
        Thread.sleep(3000);

        driver.navigate().forward();
        Thread.sleep(3000);
        String productName = driver.findElement(By.xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[2]/div[1]/a[1]/div[1]")).getText();
        System.out.println(productName);

        driver.close();
    }
}
//login-button