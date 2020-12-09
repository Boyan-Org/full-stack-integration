import LoginForm from "@/components/LoginForm.vue";
import {shallowMount} from "@vue/test-utils";

const $router = {
    replace: jest.fn()
}

describe("LoginFrom.vue", () => {
    let wrapper;

    beforeEach(() => {
        wrapper = shallowMount(LoginForm, {
            mocks:{
                $router
            }
        })
    })

    it("check router go to the right place", ()=> {
        // expect(wrapper.contains("el-button")).toBe(true);
        wrapper.find("el-button").trigger("click");
    })

})