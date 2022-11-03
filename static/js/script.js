




document.addEventListener("DOMContentLoaded", () => {
    load_complete(); 
  });


load_complete = () => {
    console.log("load complete!")
}

document.getElementById("send_btn").addEventListener("click",() => {
    let the_url = document.getElementById("the_url").value
    //單行判斷式，the_url是否為真
    the_url ? got_url(the_url) : do_alert()
})

got_url = async(the_url) => {
    console.log("縮網址送出")
    document.getElementById("alerts").innerHTML="已送出"
    //第一步先確認之前是否有相同得的url 使用 get request 查詢
    //若有，GET返回資料，若無，POST新增資料
    const options = {method: "GET"};
    const response = await fetch("/api/get_url?url_here="+the_url,options)
    const result = await response.json();
    if(result.ok_get){
        console.log("We have this url before",result.ok_get)
        show_the_shorted_url(result.ok_get)
    }else if(result.ok_not_get){
        console.log("This is a new url",result.ok_not_get)
        show_the_shorted_url(result.ok_not_get)
    }else{
        console.log("something wrong happend")
        document.getElementById("shorted_url").innerHTML = "Errored!"
    }
}

do_alert = () => {
    document.getElementById("alerts").innerHTML="你沒輸入"
}

show_the_shorted_url = (url) => {
    place = document.getElementById("shorted_url")
    place.innerHTML = "www.vivien.fun/" + url
}