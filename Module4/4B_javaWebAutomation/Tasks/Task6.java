package Tasks;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Task6 {
    public static void main(String[] args) throws InterruptedException {
        System.setProperty("webdriver.chrome.driver", "C:\\Users\\odunuga\\kehinde-testify\\SeleniumWeb\\src\\chromedriver.exe");

        //Launch browser
        WebDriver driver = new ChromeDriver();

        //Maximize the browser
        driver.manage().window().maximize();

        //Navigate to the url
        driver.get("https://www.saucedemo.com/");
        Thread.sleep(3000);

        //Login
        driver.findElement(By.cssSelector("input#user-name")).sendKeys("problem_user");
        driver.findElement(By.cssSelector("input#password")).sendKeys("secret_sauce");
        Thread.sleep(2000);
        driver.findElement(By.cssSelector("input#login-button")).click();
        Thread.sleep(2000);

        //Add to cart
        driver.findElement(By.cssSelector("button#add-to-cart-sauce-labs-onesie")).click();
        Thread.sleep(2000);

        //View cart
        driver.findElement(By.cssSelector("a.shopping_cart_link")).click();
        Thread.sleep(2000);

        //Checkout
        driver.findElement(By.cssSelector("button#checkout")).click();
    }
}
