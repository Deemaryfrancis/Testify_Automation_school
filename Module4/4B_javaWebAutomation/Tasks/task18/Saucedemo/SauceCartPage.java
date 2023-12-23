package pageObjectModel;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

public class SauceCartPage {
    WebDriver Sdriver=null;
    public SauceCartPage(WebDriver driver){
        Sdriver = driver;
        PageFactory.initElements(Sdriver, this);
    }
    @FindBy(xpath = "//span[contains(text(),'3')]")
    private WebElement cart;
    public WebElement getCart(){
        return cart;
    }
    @FindBy(linkText = "Sauce Labs Onesie")
    private WebElement item1;
    public WebElement getItem1(){
        return item1;
    }
    @FindBy(linkText = "Sauce Labs Bike Light")
    private WebElement item2;
    public WebElement getItem2(){
        return item2;
    }
    @FindBy(linkText = "Sauce Labs Fleece Jacket")
    private WebElement item3;
    public WebElement getItem3(){
        return item3;
    }
}