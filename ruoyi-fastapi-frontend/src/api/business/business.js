import request from '@/utils/request'
// Member api
export function getMemberList() {
    return request({
        url: '/business/members',
        method: 'get',
    })
}

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

export function updateClient(data) {
    return request({
        url: '/business/update_clients',
        method: 'post',
        data: data
    })
}
// Provider api
export function getProviderList() {
  return request({
    url: '/business/providers',
    method: 'get',
  })
}
export function createProvider(data) {
    return request({
        url: '/business/add_providers',
        method: 'post',
        data: data
    })
}

// Quotation api
export function getQuotationList() {
  return request({
    url: '/business/quotations',
    method: 'get',
  })
}
export function createQuotation(data) {
    return request({
        url: '/business/add_quotations',
        method: 'post',
        data: data
    })
}

// Task api
export function getTaskList() {
  return request({
    url: '/business/tasks',
    method: 'get',
  })
}
export function createTask(data) {
    return request({
        url: '/business/add_tasks',
        method: 'post',
        data: data
    })
}
export function updateTask(data) {
    return request({
        url: '/business/update_tasks',
        method: 'post',
        data: data
    })
}