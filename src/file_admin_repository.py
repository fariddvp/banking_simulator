from src.admin_repository import AdminRepository
import os

class FileAdminRepository(AdminRepository):
    def __init__(self, path):
        self.path = path

    def create_admin(self, admin):

        if not os.path.exists(self.path):
            with open(self.path, 'a') as f:
                f.write(f'{admin.nationality_code}#'
                        f'{admin.password}#'
                        f'{admin.first_name}#'
                        f'{admin.last_name}\n')
                print(f'\n*** Hi, {admin.first_name} {admin.last_name}, '
                    f'You Registered as Admin with Nationality Code: {admin.nationality_code}')
                input('Press any Key to Return Admin Option.')
                return
        else:
            with open(self.path, 'r') as r:
                admin_info = r.read().split('#')
                if admin_info[0] == admin.nationality_code:
                    print(f'\n*** Warning: You Already Signed Up with Nationality Code: ({admin.nationality_code})')
                    input('Press any Key to Return Admin Option.')
                    return
                
                elif admin_info[0] != '' and admin_info[1] != '':
                    print('\n*** Warning: Already an Admin Registered and You Can not Add as another Admin, Please Login.')
                    input('Press any Key to Return Admin Option.')
                    return

                else:
                    with open(self.path, 'w') as f:
                        f.write(f'{admin.nationality_code}#'
                                f'{admin.password}#'
                                f'{admin.first_name}#'
                                f'{admin.last_name}\n')
                        print(f'\n*** Hi, {admin.first_name} {admin.last_name}, '
                            f'You Registered as Admin with Nationality Code: {admin.nationality_code}')
                        input('Press any Key to Return Admin Option')
                        return




        