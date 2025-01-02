import request from '@/utils/request'

// project api
export function getProjectList() {
  return request({
    url: '/business/projects',
    method: 'get',
  })
}

export function getClientList() {
  return request({
    url: '/business/clients',
    method: 'get',
  })
}
export function createClient(data) {
    return request({
        url: '/business/add_clients',
        method: 'post',
        data: data
    })
}

export function deleteClient(data) {
    return request({
        url: '/business/delete_clients',
        method: 'post',
        data: data
    })
}

